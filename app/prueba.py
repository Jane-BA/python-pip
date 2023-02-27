import csv

#donde se ubica el archivo
def prueba(path):
    
    #abre el archivo en csvfile con el permiso de lectura
    with open(path, 'r') as csvfile:
        
        #lee y convierte el archivo en una lista y lo guarda en reader
        reader = csv.reader(csvfile,delimiter=',')
        print(reader)
        print('... 1 ...')

    ### Convertirlo a Diccionario ###
        #Genera un array de las llaves
        header = next(reader)
        print(header)
        print('... 2 ...')

        data = []
        #genera un array de valores y al final separa los paises con ****
        for row in reader:
            #Union de ambos arrays, convirtiendolo en un array de tupplas
            iterable = zip(header, row)
            print(iterable)
            print('... 3 ...')

            #Lo convierto a diccionario
            country_dict ={key:value for key,value in iterable}
            print(country_dict)
            print('... 4 ...')
            
            #Crear una lista de diccionarios con clave valor para poderlo consultar
            data.append(country_dict)
        
        return data



# Para usar el archivo como un script
if __name__=='__main__':
    data = prueba('./app/pru.csv')
    print(data[0])