import imaplib

EMAIL = 'gamexconsoles@gmail.com'
PASSWORD = '252943Qmm'
SERVER = 'imap.gmail.com'

mail = imaplib.IMAP4_SSL(SERVER)
mail.login(EMAIL, PASSWORD)

mailboxResponse= mail.lsub("[Gmail]")
mailboxes=mailboxResponse[1]
print("\n")
print(mailboxes)
print("\n")

#getmailbox name
for mailbox in mailboxes:
    mailboxName = mailbox.split()
    
    mailboxName[3] = str(mailboxName[3]).replace("b","") 
    mailboxName[3] = str(mailboxName[3]).replace("'","")
    print(str(mailboxName[3]))


mail.select()

#.lsub("aca va el parecido")  sirve para listar los mailboxes disponibles
#.select("nombre de la mailbox") sirve para entrar en la mailbox deseada