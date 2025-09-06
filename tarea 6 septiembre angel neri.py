print ("describe un programa que determine si una persona tiene la edad")
print("suficiente para votar y si esta incristo en el cne")

edad = int(input("ingresa su edad: "))
inscrito = input ("¿estas registrado en el cne?").lower()

if edad >= 18 and inscrito == "si" :
 print("usted tiene la edad suficiente para votar y esta inscristo en el CNE.")
else:
 print("usted no cumple con los requisitos para votar.")
