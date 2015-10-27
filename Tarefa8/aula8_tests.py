__author__ = 'Liu'

import unittest
from Tarefa8.anagrama import Anagrama


class AnagramaTests(unittest.TestCase):

    '''
    '' e '' retorna verdadeiro
    ' ' e '' retorna verdadeiro
    'a' e 'a' retorna verdadeiro
    'a' e 'a     ' retorna verdadeiro
    'ab' e 'ab' retorna verdadeiro
    'ba' e 'ab' retorna verdadeiro
    'b   a' e 'ab' retorna verdadeiro
    'ba' e 'a' retorna falso
    '''
    def test_string_vazio(self):
        anagrama = Anagrama('', '')
        self.assertTrue(anagrama.comparar_string())

    def test_espaco(self):
        anagrama = Anagrama(' ', '')
        self.assertTrue(anagrama.comparar_string())
        anagrama = Anagrama('a', 'a      ')
        self.assertTrue(anagrama.comparar_string())

    def test_comparar_string(self):
        anagrama = Anagrama('a', 'a')
        self.assertTrue(anagrama.comparar_string())
        anagrama = Anagrama('ab', 'ab')
        self.assertTrue(anagrama.comparar_string())
        anagrama = Anagrama('roma', 'amor')
        self.assertTrue(anagrama.comparar_string())
        anagrama = Anagrama('ba', 'ab')
        self.assertTrue(anagrama.comparar_string())
        anagrama = Anagrama('b', 'ab')
        self.assertFalse( anagrama.comparar_string())
        anagrama = Anagrama('ba', 'a')
        self.assertFalse(anagrama.comparar_string())


if __name__ == "__main__":
    unittest.main()
