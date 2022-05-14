from statistics import median, mode, pstdev, variance, pstdev
print("Bienvenido a calcEstadistica \n")
datos_estudio = [] # Inicializamos la lista que contiene los datos de la muestra.
datos_muestra = int(input("Introduzca el primer dato de la muestra a estudiar: "))
datos_estudio.append(datos_muestra)
while input("¿Existen mas datos a estudiar? [S/N]") == "S":
    datos_muestra = int(input("Introduzca el primer dato de la muestra a estudiar: "))
    datos_estudio.append(datos_muestra) # Introducimos los datos y los almacenamos en la lista previamente definida.
datos_estudio.sort()
media = sum(datos_estudio) / len(datos_estudio) # Calculamos la media.
mediana = median(datos_estudio) # Calculamos la mediana.
moda = mode(datos_estudio) # Calculamos la moda.
varianza = variance(datos_estudio) # Calculamos la varianza.
desviacion_tipica = pstdev(datos_estudio) # Calculamos la desviación típica.
print("La media es {}, la mediana es {}, la moda es {}, la varianza es {} y la desviación típica es {}".format(media, mediana, moda, varianza, desviacion_tipica))