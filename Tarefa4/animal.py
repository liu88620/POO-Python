
__author__ = 'Liu'

class Animal():

    def __init__(self, raca, peso, idade):
        self.raca = raca
        self.peso = peso
        self.idade = idade


    def fazerBarulho(self):
        pass

class Cachorro(Animal):
    def fazerBarulho(self):
        print('Au au!')

class Gato(Animal):
    def fazerBarulho(self):
        print('Miau~')

class Passaro(Animal):
    def fazerBarulho(self):
        print('Piu piu')

class Peixe(Animal):
    def fazerBarulho(self):
        print('Blu blu')


cao = Cachorro('Pastor Alemao', 5.0, 5 )
cao.fazerBarulho()
gato = Gato('Siames', 1.0, 5)
gato.fazerBarulho()
passaro = Passaro('Arara Azul', 0.3, 2 )
passaro.fazerBarulho()
peixe = Peixe('Tubarao Azul', 500.0, 50)
peixe.fazerBarulho()

