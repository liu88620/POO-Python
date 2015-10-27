__author__ = 'Liu'

import unittest
from Tarefa7.animal import Animais, Animal, Cachorro, Gato, Passaro, Peixe

class MyTestCase(unittest.TestCase):

    def test_ordena_peso(self):
        a1 = Cachorro('Pastor Alemao', 5.0, 5)
        a2 = Gato('Siames', 1.0, 5)
        a3 = Passaro('Arara Azul', 0.3, 2)
        a4 = Peixe('Tubarao Azul', 500.0, 50)

        animais = Animais(a1, a2, a3, a4)
        animais.ordenar_peso()
        self.assertEqual([a3, a2, a1, a4], animais)

    def test_ordena_nome(self):
        a1 = Cachorro('Pastor Alemao', 5.0, 5, 'Dodo')
        a2 = Gato('Siames', 1.0, 5, 'Mimi')
        a3 = Passaro('Arara Azul', 0.3, 2, 'Piupiu')
        a4 = Peixe('Tubarao Azul', 500.0, 50, 'Blue')

        animais = Animais(a1, a2, a3, a4)
        animais.ordenar_nome()
        self.assertEqual([a4, a1, a2, a3], animais)


if __name__ == '__main__':
    unittest.main()
