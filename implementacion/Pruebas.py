import imaplib

EMAIL = 'dummym1@outlook.es'
PASSWORD = '252943Qmm'
SERVER = 'outlook.office365.com'


mail = imaplib.IMAP4_SSL(SERVER)
mail.login(EMAIL, PASSWORD)

mailboxResponse= mail.list()
mailboxes=mailboxResponse[1]
print("\n")
print(mailboxes)
print("\n")

#getmailbox name
for mailbox in mailboxes:
    mailboxName = mailbox.split()
    
    print("\n")
    print(mailboxName)
    print("\n")

    finalbox = str(mailboxName[len(mailboxName) - 1]).replace("b","") 
    finalbox = finalbox.replace("'","")
    print(finalbox)


#.lsub("aca va el parecido")  sirve para listar los mailboxes disponibles
#.select("nombre de la mailbox") sirve para entrar en la mailbox deseada