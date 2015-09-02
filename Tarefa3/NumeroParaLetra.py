# coding:950
__author__ = 'Liu'

def numeroParaLetra(numero1):
    lista = []
    numero_para_letra = {
        1:'um', 2:'dois', 3:'tres', 4:'quatro', 5:'cinco', 6:'seis', 7:'sete', 8:'oito', 9:'nove', 0:'zero'
    }
    for n in str(numero1):
        n = int(n)
        lista.append(numero_para_letra[n])

    return lista

print(numeroParaLetra(123))
print(numeroParaLetra(456))
print(numeroParaLetra(789))
print(numeroParaLetra(101))
