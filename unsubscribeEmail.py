import imaplib, os, email, re, webbrowser
from bs4 import BeautifulSoup #type: ignore
from email.header import decode_header
from dotenv import load_dotenv #type: ignore

load_dotenv(override=True)

email_user = os.getenv("EMAIL_USER")
email_password = os.getenv("EMAIL_PASSWORD")
links_file_path = os.getenv("LINKS_FILE_PATH")


mail = imaplib.IMAP4_SSL("imap.gmail.com")
mail.login(email_user, email_password)

def sanitize_filename(s):
    s = s.strip()
    s = s.replace("\r", "").replace("\n", " ")
    return re.sub(r'[\\/*?:"<>|]', "_", s)

def sanitize_from(f):
    f = f.strip()
    f = f.replace('<', " ").replace(">", " ")
    return f

def sanitize_link(l):
    l = l.strip()
    l = l.replace("\\r", "").replace("\\n", "")
    return re.sub(r'["]', "", l)

try:
    mail.noop()
    print("connected")

    mail.select("INBOX")
    status, data = mail.search(None, 'TEXT Unsubscribe')

    message_ids = data[0].split()

    for id in range(len(message_ids)):
        status, msg_data = mail.fetch(message_ids[id], '(RFC822)')

        raw_email = email.message_from_bytes(msg_data[0][1])

        subject, encoding = decode_header(raw_email['Subject'])[0]

        from_ = raw_email.get("FROM")
        print(f"from: {from_}")
        print(f"subject: {subject}")

        if isinstance(subject, bytes):
            subject = subject.decode(encoding or "utf-8")

        for part in raw_email.walk():
            content_type = part.get_content_type()
            print(content_type)
            if content_type == 'text/html':
                pl = str(part.get_payload(decode=True))
                # print(pl)
                soup = BeautifulSoup(pl, "html.parser")

                print(soup.prettify())

                found = soup.a
                if found == None:
                    continue

                print(found.prettify())
                print("---------------------------------------------------------------------END----------------------------------------------------------")

                for link in soup.find_all('a'):
                    anchor_text = link.get_text()
                    pattern = re.compile(r'\bunsubscribe\b', re.IGNORECASE)
                    result = re.findall(pattern=pattern, string=anchor_text)
                    if result:
                        safe_subject = sanitize_filename(subject)
                        safe_from = sanitize_from(from_)
                        link_u = link.get('href')
                        safe_link = sanitize_link(link_u)
                        
                        print(f"found match: {result}")
                        print()
                        # print(link.get('href'))
                        with open(links_file_path, 'r+') as f:
                            file = f.read()
                            if file == "":
                                f.write(f'\n\n<p>{safe_from}:</p>\n <a href="{safe_link}">unsubscribe</a>')   
                            else:
                                if safe_from not in file:
                                    f.write(f'\n\n<p>{safe_from}:</p>\n <a href="{safe_link}">unsubscribe</a>')
                                else:
                                    f.close()

                                            
        if id == 20:
            break

    mail.close()
    mail.logout()
    print("Logged out")

    file_path = os.path.abspath('unsubscribeLinks\\links.html')
    webbrowser.open(f'file://{file_path}')

    # file_path = os.path.abspath('unsubscribeLinks\\links.html')
    # with open(file_path, 'r') as f:
    #     link_file = f.read()
    #     soup = BeautifulSoup(link_file, "html.parser") 
    #     for link in soup.find_all('a'):
    #         link = link.get('href')  
    #         webbrowser.open(link)  
except imaplib.IMAP4_SSL.error as e:
    print(f"Error: {e}")
    mail.close()
    mail.logout()


