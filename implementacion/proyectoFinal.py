import imaplib
from operator import truediv

#embellecedor y bienvenida
print("\n" * 9)
print("Binevenido a la interfaz basada en texto para usar IMAP")
print("porfavor ingrese su email y contraseña a continuacion")

imap = imaplib.IMAP4_SSL('imap.gmail.com')

while True:
    email = 'gamexconsoles@gmail.com'#input("Email:   ")
    password = '252943Qmm' #input("Password:   ")
    try:
        imap.login(email, password)
        print("\n" * 5)
        break
    except Exception:
        print("contraseña o usuario incorrecto ")
        print("\n")


mailBoxes = imap.lsub("[Gmail]")
mailBoxes = mailBoxes[1]
mailBoxOptions = ["INBOX"]
print('"INBOX"')
#getmailbox name
for mailBox in mailBoxes:
    mailBoxName = mailBox.split()
    
    mailBoxName[3] = str(mailBoxName[3]).replace("b","") 
    mailBoxName[3] = str(mailBoxName[3]).replace("'","")
    print(str(mailBoxName[3]))

    mailBoxName[3] = str(mailBoxName[3]).replace('"','') 
    mailBoxOptions.append(str(mailBoxName[3]))

#bandejas de entrada
print("")
print("elija la bandeja de entrada que desea revisar")
while True:
    respuesta = input()
    if respuesta in mailBoxOptions:
        print("\n")
        print("accediendo a la baneja " + respuesta) 
        imap.select('[Gmail]/Borradores')
        break
    elif respuesta.upper() in mailBoxOptions:
        print("\n")
        print("accediendo a la baneja " + respuesta.upper()) 
        imap.select('[Gmail]/Borradores')
        break
    else:
        print("\n" * 3)
        print("no posee esa badeja, intente denuevo")
        print("las bandejas disponibles son:")

        for i in range(len(mailBoxOptions)):
            print('"' + mailBoxOptions[i] + '"')
        
while True:
    print("desea filtrar los mails en esta bandeja?s/n")
    respuesta = input()
    if respuesta == "s"  or respuesta == "si" or respuesta == "y" or respuesta == "yes":
        break
    elif respuesta == "n"  or respuesta == "no":
        break

