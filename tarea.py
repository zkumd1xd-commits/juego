print("CALCULADORA SIMPLE//")
operacion = input ("Elige la operacion que deseas realizar (SUMA, RESTA ,DIVISION, MULTIPLICACION").upper()

if  operacion == "SUMA":
    numero_1 = float(input ("ingresa el primer numero: "))
    numero_2 =float(input("ingresa el segundo numero: "))
     
    resultado = numero_1 + numero_2
    print(f"el numero de la suma es : {resultado}")

if operacion == "RESTA":
    numero_3 = float(input ("ingresa el primer numero:"))
    numero_4 = float(input("ingresa el segundo numero:"))
    resultado_1 = numero_3 - numero_4
    print(f"el numero de la resta es : {resultado_1}")

if operacion == "DIVISION":
    numero_5 = float(input ("ingresa el primer numero"))
    numero_6 = float (input ("ingresa el primer numero"))
    resultado_2 = numero_5 / numero_6
    print(f"el numero de la DIVISION es: {resultado_2}")

if operacion =="MULTIPLICACION":
    numero_7 = float(input ("ingresa el primer numero"))
    numero_8 = float(input ("ingresa el primer numero"))
    resultado_3 = numero_7 * numero_8
    print(f"el numero de la MULTIPLICACION es : {resultado_3}")