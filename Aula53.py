"""
enumerate - enumera iteraveis (indices)

"""

lista = ['Maria', 'Helena', 'Luis']
lista.append('Vanio')

# lista_enumerada = enumerate(lista)

for indice, nome in enumerate(lista):
    print(indice, nome)

# for item in enumerate(lista):
#     indice, nome = item
#     print(indice, nome)

# for tupla_enumerada in enumerate(lista):
#     print('For da tupla: ')
#     for valor in tupla_enumerada:
#         print(f'\t {valor}')
