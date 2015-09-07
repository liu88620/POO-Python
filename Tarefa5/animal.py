__author__ = 'Liu'

class Animal():

    def __init__(self, raca, peso, idade):
        self.raca = raca
        self.peso = peso
        self.idade = idade

    def __repr__(self):
        return self.raca

    def fazerBarulho(self):
        pass

class Cachorro(Animal):
    def fazerBarulho(self):
        print('Au au!')

class Gato(Animal):
    def fazerBarulho(self):
        print('Miau~')


cao = Cachorro('Pastor Alemao', 5.0, 5 )
cao.fazerBarulho()
gato = Gato('Siames', 1.0, 5)
gato.fazerBarulho()
