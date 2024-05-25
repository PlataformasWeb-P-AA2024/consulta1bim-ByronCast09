import csv
from pymongo import MongoClient

client = MongoClient('localhost', 27017)
db = client['consulta01']  #este es el nombre de la base de datos
collection = db['tennis']  # este es el nombre de la coleccion que creé en la base de MongoDB

data = [] #cada fila se convierte en un diccionario que se agrega a data
with open('atp_tennis.csv', mode='r', encoding='utf-8-sig') as file:
    csv_reader = csv.DictReader(file)
    for row in csv_reader:
        data.append(row)

collection.insert_many(data)

# Consulta de cuantos documentos hay 
documentosTotal = collection.count_documents({})  
print(f"Numero de documentos totales: {documentosTotal}")

#for document in documentosTotal:
 #   print(f"Numero total de documentos es: {documentosTotal}")
