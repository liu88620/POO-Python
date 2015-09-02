# coding:950
__author__ = 'Liu'

def letraParaNumero(list_numerais):
    resultado = ''
    letra_para_numero = {
        'um':'1', 'dois':'2', 'tres':'3', 'quatro':'4', 'cinco':'5', 'seis':'6', 'sete':'7', 'oito':'8', 'nove':'9', 'zero':'0'
    }

    for numeral in list_numerais:
        resultado += letra_para_numero[numeral]

    return resultado

print(letraParaNumero(['um', 'dois', 'tres']))
print(letraParaNumero(['quatro', 'cinco', 'seis']))
print(letraParaNumero(['sete', 'oito', 'nove']))
print(letraParaNumero(['um', 'zero', 'tres']))



