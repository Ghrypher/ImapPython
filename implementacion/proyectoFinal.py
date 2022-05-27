import imaplib
import email
import getpass

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

    if not complejo: #Muestra todas las opciones de los filtros simples
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
            try: #Solicita el filtro que desea usar y lo busca en el diccionario
                opcion = input("deseo utilizar el filtro numero:   ")
                opcion = filtrosSimples[int(opcion)]
                break
            except:
                print("El valor ingresado no era un numero o excedio el numero de opciones. Ingrese un numero")

    else: #Muestra todas las opciones de los filtros complejos

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
        15- No usar filtro
        """)

        while True:
            try: #Solicita el filtro que desea usar y lo busca en el diccionario. Luego solicita el argumento para el filtro
                opcion = input("deseo utilizar el filtro numero:   ")
                opcion = filtrosComplejos[int(opcion)]
                
                if opcion == "ALL":
                    break

                argumento = input("Ingrese el argumento correspondiente para el filtro elegido ")

                break
            except:
                print("El valor ingresado no era un numero o excedio el numero de opciones. Ingrese un numero")

    return opcion, argumento

#embellecedor y bienvenida
print("\n" * 9)
print("Binevenido a la interfaz basada en texto para usar IMAP con gmail")


imap = imaplib.IMAP4_SSL('imap.gmail.com') #Indica y setea que protocolo va a utilizar 

while True:
    respuesta = input("Desea usar una cuenta preconfiguarada?(s/n)   ")

    if respuesta in ["s", "y", "si", "yes"]: #Carga la cuenta predeterminada
        user = 'gamexconsoles@gmail.com'
        password = 'khdugnhuxiiktrej' 

    elif respuesta in ["n", "no"]: #Solicita el usuario y contraseña para poder ingresar a la cuenta
        print("""(tenga en cuenta que de no estar configurada su cuenta es probable que no pueda iniciar sesion)
        
        porfavor ingrese su email y contraseña a continuacion
         """)
        user = input("Email:   ")
        password = getpass.getpass("Password:   ")

    else:
        print ("\nrespuesta esconocida\n")
        continue

    try: #Se logea a la cuenta con el usuario y contraseña ingresados
        imap.login(user, password)
        print("\n" * 5)
        break

    except Exception:
        print("contraseña o usuario incorrecto ")
        print("\n")


mailBoxes = imap.list() #Obtiene una tupla con un "OK" y una lista con todas las carpetas del correo
mailBoxes = mailBoxes[1] #Extrae la las carpetas del correo
mailBoxOptions = []

#getmailbox name
for mailBox in mailBoxes: 
    mailBoxName = mailBox.split() #Separa las diferentes carpetas del mail

    #Obtiene una de las carpetas y las aprolija removiendo letras y caracteres innecesarios
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
    respuesta = input("utilizar la bandeja ") #Solicita ingresar una de las carpetas obtenidas anteriormente

    #Verifica si el valor ingresado es valido e ingresa a la carpeta especificada
    if respuesta in mailBoxOptions: 
        print("\n")
        print("accediendo a la baneja " + respuesta) 
        imap.select(respuesta)
        break

    #Verifica si el valor ingresado es valido e ingresa a la carpeta especificada
    elif respuesta.upper() in mailBoxOptions:
        print("\n")
        print("accediendo a la baneja " + respuesta.upper()) 
        imap.select(respuesta.upper())
        break

    #Verifica si el valor ingresado es valido e ingresa a la carpeta especificada
    elif ("[Gmail]/" + respuesta) in mailBoxOptions:
        print("\n")
        print("accediendo a la baneja " + ("[Gmail]/" + respuesta)) 
        imap.select(("[Gmail]/" + respuesta))
        break

    #Solicita una carpeta valida y vuelve a mostrar las opciones
    else:
        print("\n" * 3)
        print("no posee esa badeja, intente denuevo")
        print("las bandejas disponibles son:")

        for i in range(len(mailBoxOptions)):
            print('"' + mailBoxOptions[i] + '"')


while True:
        print("\n")
        print("Desea filtrar los mails en esta bandeja?s/n") 
        
        respuesta = input()
        argumento= ""

        if respuesta in ["s", "y", "yes", "si"]:
            while True:

                print("\n")
                print("Desea utilizar filtros complejos? s/n")
                respuesta = input()

                if respuesta in ["s", "si", "y", "yes"]:
                    print("\nIniciando filtros complejos...")
                    filtro, argumento = seleccionarFiltro(True)
                    break

                elif respuesta in ["n", "no"]:
                    print("\nIniciando filtros simples...")
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
    status, data = imap.search(None, filtro) #Busca en el mail los correos que coincidan con el filtro seleccionado
else:
    status, data = imap.search(None, filtro, argumento) #Busca en el mail los correos que coincidan con el filtro seleccionado y el argumento para dicho filtro

idsMail = []
for bloque in data: #Recorre cada bloque de informacion con ids de los mails
    idsMail += bloque.split() #Separa el bloque en una lista que contiene los diferentes ids por separado

for i in idsMail:

    status, data = imap.fetch(i, '(RFC822)') #Busca y obtiene informacion del mail en base al id del mismo

    for response_part in data: #Data contiene una lista de tuplas con el cabezal, contenido y cierre 
        if isinstance(response_part, tuple): #Si es una tupla
            message = email.message_from_bytes(response_part[1]) #Buscamos directamente el contenido del mail 

            mail_from = message['from'] #Obtenemos quien envio el mail
            mail_subject = message['subject'] #Obtenemos el asunto del mail

            if message.is_multipart(): #Si el contenido es multiparte, significando que tiene texto plano y otros datos como anexos o codigo html
                mail_content = ''

                for part in message.get_payload(): #Recorremos parte por parte el mail
                    
                    #Si es texto plano lo extraemos
                    if part.get_content_type() == 'text/plain':
                        mail_content += part.get_payload()
            else:
                
                #Si es puro texto plano entonces lo extraemos todo de una
                mail_content = message.get_payload() 

            print(f'From: {mail_from}') #Quien envio el mail
            print(f'Subject: {mail_subject}') #Asunto del mail
            print(f'Content: {mail_content}') #Contenido del mail
