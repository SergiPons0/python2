def llbc(ll,c):
    n=[]
    for x in ll:
        if x[:1]==c:
            n.append(x)
    return n
print(llbc(['sabo','taula','teclat','ratoli','tren'],'s'))

def a(llista,lletra):
    return list(filter(lambda a: a[:1]==lletra,llista))
print(a(['maria','manta','peu'],'p'))