print("Bienvenido a calcEstadistica \n")
datos_estudio = []
datos_muestra = int(input("Introduzca el primer dato de la muestra a estudiar: "))
datos_estudio.append(datos_muestra)
while input("¿Existen mas datos a estudiar? [S/N]") == "S":
    datos_muestra = int(input("Introduzca el primer dato de la muestra a estudiar: "))
    datos_estudio.append(datos_muestra)
media = sum(datos_estudio) / len(datos_estudio)
