"""
Introdução ao desecompacotamento + tuples (tuplas)

"""

lista = ['Luiz', 'Maria', 'Vanio']

nome1, nome2, nome3 = ['Luiz', 'Maria', 'Vanio']

# nome1, *resto = ['Luiz', 'Maria', 'Vanio']

_, nome1, *_ = ['Luiz', 'Maria', 'Vanio']
print(nome1)