"""
Introdução ao Try/Except

"""

numero_str = input ('Vou dobrar o número que digitar: ')

try:
    print('STR: ', numero_str)
    numero_float = float(numero_str)
    print("FLOAT: ", numero_float)
    print(f'o dobro de {numero_str} é {numero_float *  2:.2f}')
except:
    print("Isso não é um número")
