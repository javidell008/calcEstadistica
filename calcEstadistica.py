from statistics import median, mode, pstdev, variance, pstdev
print("Bienvenido a calcEstadistica \n")
datos_estudio = [] # Inicializamos la lista que contiene los datos de la muestra.
num_estudio = int(input("¿Cuantos datos componen la muestra a estudiar?"))
for i in range(1, num_estudio + 1):
    datos_muestra = int(input("Introduzca el dato de la muestra a estudiar: "))
    datos_estudio.append(datos_muestra) # Introducimos los datos y los almacenamos en la lista previamente definida.
datos_estudio.sort()
media = sum(datos_estudio) / len(datos_estudio) # Calculamos la media.
mediana = median(datos_estudio) # Calculamos la mediana.
moda = mode(datos_estudio) # Calculamos la moda.
varianza = variance(datos_estudio) # Calculamos la varianza.
desviacion_tipica = pstdev(datos_estudio) # Calculamos la desviación típica.
print("La media es {}, la mediana es {}, la moda es {}, la varianza es {} y la desviación típica es {}".format(media, mediana, moda, varianza, desviacion_tipica))
