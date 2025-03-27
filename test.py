import imaplib
import email
from email.header import decode_header

mail = imaplib.IMAP4_SSL('imap.gmail.com')
mail.login('meirstroh6@gmail.com', 'dwfoardkpejpeela')
mail.select('inbox')

mail.create("checked")

mail.logout()