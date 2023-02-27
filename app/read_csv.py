import csv

#donde se ubica el archivo
def read_csv(path):
    
    #abre el archivo en csvfile con el permiso de lectura
    with open(path, 'r') as csvfile:
        
        #lee y convierte el archivo en una lista y lo guarda en reader
        reader = csv.reader(csvfile,delimiter=',')
        
    ### Convertirlo a Diccionario ###
        #Genera un array de las llaves
        header = next(reader)

        data = []
        #genera un array de valores y al final separa los paises con ****
        for row in reader:
            #Union de ambos arrays, convirtiendolo en un array de tupplas
            iterable = zip(header, row)

            #Lo convierto a diccionario
            country_dict ={key:value for key,value in iterable}

            #Crear una lista de diccionarios con clave valor para poderlo consultar
            data.append(country_dict)
        
        return data



# Para usar el archivo como un script
if __name__=='__main__':
    data = read_csv('./app/data.csv')
    print(data[0])