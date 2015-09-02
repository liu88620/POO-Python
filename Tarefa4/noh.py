__author__ = 'Liu'

class Noh():
     def __init__(self, proximo=None):
         self.proximo = proximo

     def get_proximo(self): ## verifica se o proximo noh eh "nulo", se nao, vai para proximo.
         if self.proximo is not None:
             return self.proximo

     def tem_proximo(self): ## verifica se tem o proximo, se nao, sai da funcao.
         if self.proximo is not None:
             return True
         return False


utimo = Noh()
no2 = Noh(utimo)
atual = Noh(no2)

while atual.tem_proximo():
    print('Tem proximo')
    atual = atual.get_proximo()
print('Fim do noh')
