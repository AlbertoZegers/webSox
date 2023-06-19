texto="hola"
def modulo(texto):
    lista_saludos=[]
    palabra="hola"
    lista_saludos.append(palabra)
    palabra="buenas"
    lista_saludos.append(palabra)
    palabra="buenos días"
    lista_saludos.append(palabra)
    palabra="buenos dias"
    lista_saludos.append(palabra)
    palabra="buenas tardes"
    lista_saludos.append(palabra)
    palabra="buenas noches"
    lista_saludos.append(palabra)
    palabra=texto
    if palabra in lista_saludos:
        resultado=f"Sox: {palabra} ¿En qué puedo ayudarte?"
        return resultado
    elif palabra=="help":
        resultado='''\tManual de usuario
Saludos aceptados:
-hola
-buenas
-buenos días
-buenas tardes
-buenas noches
            '''
        return resultado
    else:
        resultado="Sox: ..."
        return resultado
print(modulo(texto.lower().strip()))
#la logica de solicitud/respuesta se hizo necesario readaptar el codigo :(