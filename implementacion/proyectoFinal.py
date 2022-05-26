import imaplib
import email
from operator import truediv

filtrosSimples = {
    1: "ANSWERED",
    2: "DELETED",
    3: "DRAFT",
    4: "FLAGGED",
    5: "NEW",
    6: "OLD",
    7: "RECENT",
    8: "SEEN",
    9: "UNANSWERED",
    10: "UNDELETED",
    11: "UNDRAFT",
    12: "UNFLAGGED",
    13: "UNSEEN",
    14: "ALL"
}

filtrosComplejos = {
    1: "BCC",
    2: "BEFORE",
    3: "BODY",
    4: "CC",
    5: "FROM",
    6: "KEYWORD",
    7: "LARGER",
    8: "NOT",
    9: "ON",
    10: "SINCE",
    11: "SMALLER",
    12: "SUBJECT",
    13: "TEXT",
    14: "TO",
    15: "ALL"
}

def seleccionarFiltro(complejo):
    opcion = ""
    argumento = ""
    if not complejo:
        print("""Binevenido al sistema de filtrado porfavor eliga un tipo de filtro de los siguientes:

        A continuacion estan todos los filtros simples:

        1- Leer todos los mails que hayan sido contestados 
        2- Leer todos los mails eliminados
        3- Leer todos los borradores
        4- Leer todos los mails marcados
        5- Leer todos los mails recientes todavia no abiertos
        6- Leer todos los mails viejos
        7- Leer todos los mails recientes
        8- Leer todos los mails ya abiertos
        9- Leer todos los mails sin contestar
        10- Leer todos los mails que no han sido eliminados
        11- Leer todos los mails que no sean borradores
        12- Leer todos los mails que no estan marcados
        13- Leer todos los mails que no han sido abiertos
        14- No usar filtro""")

        while True:
            try:
                opcion = input("deseo utilizar el filtro ")
                opcion = filtrosSimples[int(opcion)]
                break
            except:
                print("El valor ingresado no era un numero o excedio el numero de opciones. Ingrese un numero")

    else:
        print("""Estos son todos los filtros complejos que requieren ingresar un argumento:

        1- Leer todos los mails que tengan el texto ingresado especificado en el campo BCC
        2- Leer todos los mails anteriores a una fecha ingresada
        3- Leer todos los mails que tengan el texto especificado en el contenido del mail
        4- Leer todos los mails que tengan el texto especificado en el campo CC
        5- Leer todos los mails hayan sido enviados por la persona especificada (para referirse a uno mismo, usar "me")
        6- Leer todos los mails que contengan la palabra clave ingresada
        7- Leer todos los mails que superen un largo especificado
        8- Leer todos los mails que no coincidan con la clave de busqueda ingresada
        9- Leer todos los mails que coincidan con la fecha ingresada
        10- Leer todos los mails enviados desde la fecha especificada hasta la fecha actual
        11- Leer todos los mails cuyo tamaño sea menor que el numero ingresado
        12- Leer todos los mails que tengan el texto ingresado como asunto
        13- Leer todos los mails que tengan el texto ingresado en la cabeza o el cuerpo del mail
        14- Leer todos los mails cuyo receptor coincida con la persona especificada
        15- No usar filtro""")

        while True:
            try:
                opcion = input("deseo utilizar el filtro ")
                opcion = filtrosSimples[int(opcion)]
                argumento = input("Ingrese el argumento correspondiente para el filtro elegido")
                break
            except:
                print("El valor ingresado no era un numero o excedio el numero de opciones. Ingrese un numero")

    return opcion, argumento


#embellecedor y bienvenida
print("\n" * 9)
print("Binevenido a la interfaz basada en texto para usar IMAP con gmail")
print("porfavor ingrese su email y contraseña a continuacion")

imap = imaplib.IMAP4_SSL('imap.gmail.com')

while True:
    user = 'gamexconsoles@gmail.com'#input("Email:   ")
    password = 'khdugnhuxiiktrej' #input("Password:   ")
    try:
        imap.login(user, password)
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
        if respuesta in ["s", "y", "yes", "si"]:
            while True:
                print("Desea utilizar filtros complejos? s/n")
                respuesta = input()
                if respuesta in ["s", "si", "y", "yes"]:
                    print("Iniciando filtros complejos...")
                    filtro, argumento = seleccionarFiltro(True)
                    break
                elif respuesta in ["n", "no"]:
                    print("Iniciando filtros simples...")
                    filtro, argumento = seleccionarFiltro(False)
                    break
                else:
                    print("Ingrese el valor correspondiente: y/n")
            break

        elif respuesta in ["n", "no"]:
            filtro = "ALL"
            break
        else:
            print("El valor ingresado no es correcto. Ingrese y/n.")

if argumento == "":
    status, data = imap.search(None, filtro)
else:
    status, data = imap.search(None, filtro, argumento)

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