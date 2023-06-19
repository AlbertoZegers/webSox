def modulo():
    import os
    import time as tm
    import random as rd
    lista_saludos=[]
    palabra="hola"
    lista_saludos.append(palabra)
    palabra="buenas"
    lista_saludos.append(palabra)
    palabra="buenos días"
    lista_saludos.append(palabra)
    palabra="buenas tardes"
    lista_saludos.append(palabra)
    palabra="buenas noches"
    lista_saludos.append(palabra)
    lista_cierres=[]
    palabra="apagate"
    lista_cierres.append(palabra)
    palabra="cierrate"
    lista_cierres.append(palabra)
    os.system("cls")
    print("IA multifuncional Sox 0.3")
    print("(Escriba help para ver el manual de usuario)")
    while True:
        palabra=str(input("Usuario: ")).lower().strip()
        if palabra in lista_saludos:
            print(f"Sox: {palabra} ¿En qué puedo ayudarte?")
        elif palabra=="help":
            os.system("cls")
            print("\tManual de usuario")
            print('''
    Saludos aceptados:
    -hola
    -buenas
    -buenos días
    -buenas tardes
    -buenas noches
    Cierres permitidos:
    -apagate
    -cierrate
    Para calcular escriba:
    -calcula
                ''')
            os.system("pause")
            os.system("cls")
            print("IA multifuncional Sox 0.3")
            print("(Escriba help para ver el manual de usuario)")
        elif palabra=="calcula":
            i=0
            numero3=0
            while True:
                i=i+1
                if i>=3:
                    operador=str(input("Sox: ingrese operador aritmetico\nUsuario: ")).strip()
                    if operador in ["+","-","*","/"]:
                        numerox=float(input(f"Sox: ingrese termino {i}\nUsuario: "))
                        if operador=="+":
                            numero3=numero3+numerox
                        elif operador=="-":
                            numero3=numero3-numerox
                        elif operador=="*":
                            numero3=numero3*numerox
                        elif operador=="/":
                            numero3=numero3/numerox
                elif i==1:
                    numero1=float(input(f"Sox: ingrese termino {i}\nUsuario: "))
                    operador=str(input("Sox: ingrese operador aritmetico\nUsuario: ")).strip()
                    while not operador in ["+","-","*","/","="]:
                        print("Error... ingrese +, -, *, / o =")
                        operador=str(input("Usuario: "))
                    if operador in ["+","-","*","/"]:
                        i=i+1
                        numero2=float(input(f"Sox: ingrese termino {i}\nUsuario: "))
                        if operador=="+":
                            numero3=(numero1+numero2)+numero3
                        elif operador=="-":
                            numero3=(numero1-numero2)+numero3
                        elif operador=="*":
                            numero3=(numero1*numero2)+numero3
                        elif operador=="/":
                            numero3=(numero1/numero2)+numero3
                if operador=="=":
                    break
            os.system("cls")
            if i==1:
                print(f"Sox: el resultado es {numero1}")
            else:
                print(f"Sox: el resultado es {numero3}")
            os.system("pause")
            os.system("cls")
            print("IA multifuncional Sox 0.3")
            print("(Escriba help para ver el manual de usuario)")
        elif palabra in lista_cierres:
            op_salir=str(input("Sox: ¿Esta seguro?(S/N)\nUsuario: ")).lower().strip()
            if op_salir=="s":
                break
        else:
            print("Sox: ...")
    os.system("cls")
    print("Cerrando modulo...")
    tm.sleep(1)
modulo()
#Aproximaciones necesarias