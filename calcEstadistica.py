from statistics import median, mode, pstdev, variance
import xlrd
import pandas as pd
print("Bienvenido a calcEstadistica \n")
archivo = input("Introduce la ruta en la que tienes almacenado tu archivo de Excel: \n")
wb = xlrd.open_workbook(archivo)

datos_estudio = [] # Inicializamos la lista que contiene los datos de la muestra.
num_estudio = int(input("¿Cuántos datos componen la muestra a estudiar?"))
hoja = wb.sheet_by_index(0) 
c = 1
while c < num_estudio:
    columna = hoja.cell_value(1, c)
    c+=1
    datos_estudio.append(columna)

datos_estudio.sort()
media = sum(datos_estudio) / len(datos_estudio) # Calculamos la media.
mediana = median(datos_estudio) # Calculamos la mediana.
moda = mode(datos_estudio) # Calculamos la moda.
varianza = variance(datos_estudio) # Calculamos la varianza.
desviacion_tipica = pstdev(datos_estudio) # Calculamos la desviación típica.
print("La media es {}, la mediana es {}, la moda es {}, la varianza es {} y la desviación típica es {}".format(media, mediana, moda, varianza, desviacion_tipica))
