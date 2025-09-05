start = print("estas caminando por un bosque oscuro y encuentras dos objetos, un fosforo y una linterna.")
opcion1 = input("¿Con cual te quedas? FOSFORO O LINTERNA: ").upper()
if opcion1 == "LINTERNA":
    print("Enciende la linterna y ves un camino iluminado. De pronto oyes algo entre los arboles")
    opcion1_1 = input("¿Quieres SEGUIR el camino o BUSCAR entre los arboles lo que hizo el ruido? ").upper()
    if opcion1_1 == "SEGUIR":
        print("Ignoras el ruido y decides seguir caminando, pero empiezas a sentir una presencia.")
        opcion1_1_1 = input("¿Que haces? ¿VOLTEAS o lo ignoras?").upper()
        if opcion1_1_1 == "VOLTEAS":
            print("Ves un animal peligroso muy cerca preparado para atacarte. Ahora estas acorralado")
   
    elif opcion1_1 == "BUSCAR":
        print("Encuentras entre los arboles un lindo conejo. ¿Lo tomas o lo dejas ir?")
        opcion1_1_2 = input("TOMAR o DEJAR: ").upper()
        if opcion1_1_2 == "DEJAR":
            print("Sigues caminando y mas adelante te encuentras a una persona. \n¿HABLAR CON ELLA? \n¿SALUDARLA? \n¿IGNORARLA? \nINSULTARLA ")
            

        

