import imaplib, os, email, re 
from bs4 import BeautifulSoup #type: ignore
from email.header import decode_header
from dotenv import load_dotenv #type: ignore

load_dotenv()

email_user = os.getenv("EMAIL_USER")
email_password = os.getenv("EMAIL_PASSWORD")


mail = imaplib.IMAP4_SSL("imap.gmail.com")
mail.login(email_user, email_password)

def sanitize_filename(s):
    s = s.strip()
    s = s.replace("\r", "").replace("\n", " ")
    return re.sub(r'[\\/*?:"<>|]', "_", s)

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

                print(found.prettify())
                print("---------------------------------------------------------------------END----------------------------------------------------------")

                for link in soup.find_all('a'):
                    anchor_text = link.get_text()
                    pattern = re.compile(r'\bunsubscribe\b', re.IGNORECASE)
                    result = re.findall(pattern=pattern, string=anchor_text)
                    if result:
                        safe_subject = sanitize_filename(subject)
                        link_u = link.get('href')
                        
                        print(f"found match: {result}")
                        print()
                        # print(link.get('href'))
                        with open(f'C:\\Users\\meir.stroh\\OneDrive\\new\\unsubscribeLinks\\links.md', 'a') as f:
                            f.write(f'\n{from_}:\n {link.get('href')}')
        if id == 20:
            break

    mail.close()
    mail.logout()
    print("Logged out")
except imaplib.IMAP4_SSL.error as e:
    print(f"Error: {e}")
    mail.close()
    mail.logout()


