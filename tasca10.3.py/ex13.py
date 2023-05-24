class Animal:
    def __init__(self,especie,edat):
        self.especie=especie
        self.edat=edat
    
    def xerrar(self):
        pass
    def mourem(self):
        pass
    def quisoc(self):
        print("sóc una {}".format(self.especie))

class Cavall(Animal):
    def xerrar(self):
        print("jjijijiji")
    def moure(self):
        print("galopa,fa trot i pas")

class Dofi(Animal):
    def xerrar(self):
        print("Txas")
    def moure(self):
        print("nadando")
        
class Abella(Animal):
    def xerrar(self):
        print("bzzzzzz")
    def moure(self):
        print("volar")
    def picar(self):
        print("si me empreñes picare")
        
class Humano(Animal):
    def xerrar(self):
        print("AAAAAAAAH")
    def moure(self):
         print("camina a dos patas")
    def __init__(self,especie,edat,nom):
        super().__init__(especie,edat)
        self.nom=nom
    def quisoc(self):
        print("Soc un huma y ma dic{}".format(self.nom))

class Hijo(Humano):
    def __init__(self,especie,edat,nom,pares):
        super().__init__(especie,edat,nom)
        self.pares=pares
    def xerrar(self):
        print("gugugaga")
    def moure(self):
        print("camina a 4 patas")
    def quisoc(self):
        print("Tomas Turbado")
    def pares(self):
        print("El meu pare es diu {} y la meva mare {}".format(self.pares[0], self.pares[1]))

class Centaure(Cavall,Humano):
    def quisoc(self):
    		 print("Sóc un centaure i sorgeix de {}".format(Centaure.__mro__))

class Xou:
    def quisoc(self):
        print("Duck type, aixo es el que soc")
    def mourem(self):
        print("Duck type, aixi em moc")
    def xerrar(self):
        print("Duck type, aixi xerr")
        
f = [Humano("Huma",32,"Joan"), Cavall("Mamifer",10), Dofi("Mamifer", 23), Abella("insecte", 1), Hijo("Huma",6,"Tomas"("Joan","Marta")), Xou(), Centaure("Centaure",40,"Quiron")]
for e in f:
    e.quisoc()
    e.mourem()
    e.xerrar()
    if type (e)==Hijo:
        e.pares()
    if type (e)==Abella:
        e.picar()