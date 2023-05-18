suma=0
a = input("Introduce un numero: ")
print("{} te {} digitos".format(a,len(a)))
for i,e in enumerate(a):
    if i%2==0:
        print("El numero parell {} es {}".format(i,e))