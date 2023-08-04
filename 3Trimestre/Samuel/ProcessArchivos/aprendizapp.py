from aprendiz import *
import csv
aprendices=[]
with open('C:\\Users\\Aprendiz.SOAAPRCIDFSP001\\Downloads\\Saber_11__2019-2.csv') as csvDataFile:
    csvReader=csv.reader(csvDataFile)
    for row in csvReader:
        objeto=aprendiz(row[0],row[1],row[2],row[3])
        print(objeto.verDatos())
        aprendices.append(objeto)
for ap in aprendices:
    print(ap.getNombre())