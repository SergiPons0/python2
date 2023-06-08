import random
import os
def menu():
    print("""
    1. Ruleta Aleatoria
    2. Lista de Tareas
    3. Juego de Adivinanzas
    4. fefef
    5. ddwed
    """)
    x= input("Introduce una opcion del menu: ")
    return x

def ruleta_aleatoria():
    lista = []
    a=0
    b=random.randint(10)
    while a != '.':
        a = input("Ingrese las opciones de la ruleta aleatoria: ")
        lista.append(random(a))
    print("La ruleta ha seleccionado la opcion de: {}".format(lista))
    return lista

def lista_de_tareas():
    listaTareas="Lista_de_Tareas"
    a=0
    while a!=".":
        a=input("Introduce los elementos de la lista de tareas: ")
        if a!=".":
            with open("/home/alumnat/Escritorio/listaTareas", "a") as archivo:
                
                archivo.write(a+"\n")
                
            
                



def adivinanzas():
    print("""
    *Las respuestas tienen que estar contestadas con la primera letra mayuscula

    -Soy un ave muy colorida,
    Con plumas brillantes y largas,
    En las noches, mi canto es oído,
    ¿Quién soy? """)

    a=input("Respuesta 1")

    print("""
    -Tengo ramas, pero no hojas,
    Un tronco, pero no es de árbol,
    ¿Qué soy? """)

    b=input("Respuesta 2: ")
    print("""
    -De noche soy blanco,
    De día me vuelvo negro,
    ¿Quién soy? 
    """)

    c=input("Respuesta 3: ")

    print("""
    -Todos me quieren tocar,
    Pero si me tocan, me destruyen,
    ¿Quién soy? 
    """)

    d=input("Respuestas 4: ")


    if a=="Pavo real":
        print("La respuesta 1 es correcta ")
    if not a=="Pavo real":
        print("La respuesta 1 es incorrecta ")
    if b=="Silla":
        print("La respuesta 2 es correcta ")
    if not b=="Silla":
        print("La respuesta 2 es incorrecta ")
    if c=="Buho":
        print("La respuesta 3 es correcta ")
    if not c=="Buho":
        print("La respuesta 3 es incorrecta ")
    if d=="Hielo":
        print("La respuesta 4 es correcta ")
    if not d=="Hielo":
        print("La respuesta 4 es incorrecta ")
    else:
        print("Gracias por jugar")
    return a, b, c, d









#PP
x="1"
while x!=".":
        x = menu()
        match x:
            case "1":
                print("Has elegido la opcion de la ruleta aleatoria" )
                Ruleta=ruleta_aleatoria()

            case "2":
                print("Has elegido la opcion de la lista de tareas")
                Lista=lista_de_tareas()
            case "3":
                print("Has elegido la opcion de el juego de las adivinanzas")
                Juego=adivinanzas()
            case "4":
                print("Has elegido la opcion de la fefefe")
                lala=lalalala()
            case "5":
                print("Has elegido la opcion de la ddwed")
                poka=pokapoka()
            case other:
                print("Opcion no valida")