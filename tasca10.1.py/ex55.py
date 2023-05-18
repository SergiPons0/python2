def mostrar(i):
    b=[]
    for e in range (i,0,-1):
        b.append(e)
    print(''.join(map(str,b)))

x= int(input("Introduce un nimero prqueño: "))
for i in range(x,0,-1):
    mostrar(i)