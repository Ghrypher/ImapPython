import imaplib

EMAIL = 'gamexconsoles@gmail.com'
PASSWORD = '252943Qmm'
SERVER = 'imap.gmail.com'

mail = imaplib.IMAP4_SSL(SERVER)
mail.login(EMAIL, PASSWORD)

mail.select('inbox')

mail_ids = []

status, data = mail.search(None, 'ALL')

for block in data:
    mail_ids += block.split()

for i in mail_ids:
    status, data = mail.fetch(i, '(RFC822)')
    print(status, data)