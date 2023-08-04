from aprendiz import *
import csv
import os 
ruta=('C:\\Users\\USER\\Downloads\\Saber_11__2019-2.csv')
aprendices=[]
with open(ruta) as csvDataFile:
    csvReader=csv.reader(csvDataFile)
    for row in csvReader:
        objeto=aprendiz(row[6],row[13],row[40],row[65],row[62])
        print(objeto.verDatos())
        aprendices.append(objeto)
for ap in aprendices:
    print(ap.getConsecutivo()) 