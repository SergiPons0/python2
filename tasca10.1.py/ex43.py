def leer_lista():
    a=[]
    x='a'
    while x!='.':
        x=input("Introduce un elemento de la lista y punto (.) para acabar: ")
        if x!='.':
            a.append(x)
    return a

def eliminar_capicua(a):
    b=[]
    if len(a)>2:
        b=a[1:-1]
    return b

x=leer_lista()
y=eliminar_capicua(x)
print("La listao riginal {} se transforma en la lista {}".format(x,y))

            