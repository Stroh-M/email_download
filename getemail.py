import imaplib, email, os
from email.header import decode_header
from dotenv import load_dotenv # type: ignore

load_dotenv()

mail = imaplib.IMAP4_SSL("imap.gmail.com")

email_user = os.getenv("EMAIL_USER")
email_password = os.getenv("EMAIL_PASSWORD")
emails_from = os.getenv("EMAILS_FROM")

mail.login(email_user, email_password)

def download_attachment(msg):
    for part in msg.walk():
            content_disposition = str(part.get_content_disposition())
            if "attachment" in content_disposition:
                filename = part.get_filename()
                if filename:
                    with open(f"\\\\MEIRLAPTOP\\downloads\\{filename}", "wb") as f:
                        f.write(part.get_payload(decode=True))
                    print("downloaded")   

try:
    mail.noop()
    print("Connection is active")

    mail.select('"INBOX"')
    status, data = mail.search(None, 'FROM', f'{emails_from}')

    email_ids = data[0].split()

    for i in range(len(email_ids)):
        status, msg_data = mail.fetch(email_ids[i], "(RFC822)")

    # print(f"{len(msg_data)}")
        msg = email.message_from_bytes(msg_data[0][1])
        # print(f"{msg}")

        subject, encoding = decode_header(msg["Subject"])[0]

        if isinstance(subject, bytes):
            subject = subject.decode(encoding or "utf-8")

        from_ = msg.get("From")

        print(f"SUBJECT: {subject}")
        print(f"FROM: {from_}")

        download_attachment(msg)
        mail.store(email_ids[i], "+X-GM-LABELS", "\\Trash")

    mail.select('"[Gmail]/Trash"')
    status, data = mail.search(None, 'FROM', f'{emails_from}')

    email_ids = data[0].split()

    for i in range(len(email_ids)):
        print(f"{i}")
        mail.store(email_ids[i], "+FLAGS", '\\Deleted')

    mail.expunge()
    
    mail.close()
    mail.logout()
    print("Logged out")
except imaplib.IMAP4_SSL.error as e:
    print(f"Connection error: {e}")
    mail.logout()
    print(f"logged out after: {e}")