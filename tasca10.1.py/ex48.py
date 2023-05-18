def crear_llista_fitxer(fitxer):
    with open(fitxer, 'r') as f:
        lista = f.readlines()
    lparaules=[linea.rstrip('\n')for linea in lista]
    print(lparaules)
    f.close()

crear_llista_fitxer('/home/cicles/AO/prova.txt')