def estar_ordenada(a):
    b=a.copy()
    a.sort()
    if a==b:
        print("la lista {} a esta ordenada {}".format(a,b))
    else:
        print("La lista {} no esta ordenada {}".format(a,b))

def leer_lista():
    a=[]
    c="a"
    while c!=".":
        c=input("Introduce un elemento de la lista y un punto para acabar:")
        if c!=".":
            a.append(c)
    return a

a=leer_lista()
estar_ordenada(a)
