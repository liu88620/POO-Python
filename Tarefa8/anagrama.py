__author__ = 'Liu'

class Anagrama():

    def __init__(self, s1, s2):
        self.s1 = s1.strip()
        self.s2 = s2.strip()

    def comparar_string(self):

        if len(self.s1) != len(self.s2):
            return False

        l1 = list(self.s1)
        l2 = list(self.s2)
        for letra in l1:
            if letra in l2:
                l2.remove(letra)
        return not l2