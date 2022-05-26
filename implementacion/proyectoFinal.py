import imaplib
import email

def seleccionarFiltro(imap):
    print("""Binevenido al sistema de filtrado porfavor eliga un tipo de filtro de los siguientes:
    1-
    2-
    3- 
    4- No usar filtro

    """)
    opcion = input("deseo utilizar el filtro ")
    return imap, "ALL"


#embellecedor y bienvenida
print("\n" * 9)
print("Binevenido a la interfaz basada en texto para usar IMAP con gmail")


imap = imaplib.IMAP4_SSL('imap.gmail.com')

while True:
    respuesta = input("Desea usar una cuenta preconfiguarada?(s/n)   ")
    if respuesta in["s", "y", "si", "yes"]:
        user = 'gamexconsoles@gmail.com'#input("Email:   ")
        password = 'khdugnhuxiiktrej' #input("Password:   ")
    else:
        print("""(tenga en cuenta que de no estar configurada su cuenta es probable que no pueda iniciar sesion)
        
        porfavor ingrese su email y contraseña a continuacion
         """)
        user = input("Email:   ")
        password = input("Password:   ")
    try:
        imap.login(user, password)
        print("\n" * 5)
        break
    except Exception:
        print("contraseña o usuario incorrecto ")
        print("\n")


mailBoxes = imap.list()
mailBoxes = mailBoxes[1]
mailBoxOptions = []

print(mailBoxes) 

#getmailbox name
for mailBox in mailBoxes:
    mailBoxName = mailBox.split()

    boxName = str(mailBoxName[(int(len(mailBoxName)) - 1)])
    boxName = boxName.replace("b","") 
    boxName = boxName.replace("'","")
    print(boxName)

    boxName = boxName.replace('"','') 
    mailBoxOptions.append(boxName)

#bandejas de entrada
print("")
print("elija la bandeja de entrada que desea revisar")
while True:
    respuesta = input("utilizar la bandeja ")
    if respuesta in mailBoxOptions:
        print("\n")
        print("accediendo a la baneja " + respuesta) 
        imap.select(respuesta)
        break
    elif respuesta.upper() in mailBoxOptions:
        print("\n")
        print("accediendo a la baneja " + respuesta.upper()) 
        imap.select(respuesta.upper())
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
            imap, filtro= seleccionarFiltro(imap)
            break
        elif respuesta == "n"  or respuesta == "no":
            filtro = "ALL"
            break


status, data = imap.search(None, filtro)

idsMail = []
for bloque in data:
    idsMail += bloque.split()

for i in idsMail:

    status, data = imap.fetch(i, '(RFC822)')

    for response_part in data:
        if isinstance(response_part, tuple):
            message = email.message_from_bytes(response_part[1])

            mail_from = message['from']
            mail_subject = message['subject']

            if message.is_multipart():
                mail_content = ''


                for part in message.get_payload():

                    if part.get_content_type() == 'text/plain':
                        mail_content += part.get_payload()
            else:

                mail_content = message.get_payload()

            print(f'From: {mail_from}')
            print(f'Subject: {mail_subject}')
            print(f'Content: {mail_content}')