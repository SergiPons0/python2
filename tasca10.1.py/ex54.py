def elements_parells(a):
    for i,e in enumerate(a):
        if i%2==1:
            print(e)
def leer_lista():
    l=[]
    a = 'a'
    while a!='.':
        a=input("Introduce una nueva palabra y punto para acabar: ")
        if a!='.':
            l.append(a)
    return l
b = leer_lista()
elements_parells(b)
