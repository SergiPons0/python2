def llegir_llista(a):
    l = [] #Creamos una lista
    for i in range(10): #Hacemos un bucle de 10 elementos, 10 recorridos
        l.append(input()) #append--> afegeix al final de la llista
                            #input--> llegim del teclat
                            #input--> sempre retorna una cadena de caracters "" o ''
    return l
    
#Programa principal
x = llegir_llista()
suma = 0
for e in x:
    suma+= int(e)
print("la suma es: ",suma)

    

