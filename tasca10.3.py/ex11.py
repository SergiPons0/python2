try:
    f=open("passwd","r")
except LookupError:
    print("Error de entrada y salida")
except:
    print("Otro tipo de error")
else: 
    print("Aqui trabajaremos con el fichero")
finally: 
    if not(f.closed): 
        f.close()

with open('/etc/passwd','r') as f:
    for line in f:
        print((line))