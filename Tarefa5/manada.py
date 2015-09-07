__author__ = 'Liu'
from animal import *

class Manada():

    def __init__(self):
        self.animais = []

    def adicicao_animal(self, animal): ## Funcao que adiciona animal
        self.animais.append(animal)

class ManadaVirgula(Manada):
    def __str__(self): ##Funcao que transforma objeto em String
        return 'ManadaVirgula'

class ManadaSustenida(Manada):
    def __str__(self):
        return 'ManadaSustenida'

## Teste
manadaVirgula = ManadaVirgula()
print(str(manadaVirgula))

manadaSustenida = ManadaSustenida()
cachorro = Animal('Rodvale', 120.0, 20)
manadaSustenida.adicicao_animal(cachorro)
print(str(manadaSustenida.animais))


##Teste de criar um classe e adiciona o animal
'''peixe = Animal("Tubarao", 100.0, 100)
manadaVirgula.adicicao_animal(peixe)
print(manadaVirgula.animais) '''

'''
##Printar a lista de cachorro
print(manadaVirgula.animais) '''


print(cachorro.raca) ## mostra a lista de cachorro




