def hay_duplicados(a):
	seen=set() 
	dupes=[x for x in a if x in seen or seen.add(x)]
	if len(dupes)>0:
		print("la lista {} tiene elementos duplicados{}".format(a,dupes))
	else:
		print("la lista {} no tiene elementos duplicados {}".format(a,dupes))

def llegir_llista():
	a=[]
	c="a"
	while c!=".":
		c=input("Introduce un elemento de la lista y punto para acabar: ")
		if c!=".":
			a.append(c)
	return a
	
#Pprincipal
a = llegir_llista()
hay_duplicados(a)
