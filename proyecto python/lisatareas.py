def lista_de_tareas():
    lista = []
    a = 1
    while a != ".":
        a = input("Ingresa una tarea para hacer: ")
        if a!=".": 
            lista.append(a)
        print("""
    Tus tareas son:
    {}""".format(lista))
    return lista