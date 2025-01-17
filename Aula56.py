"""
split e join com list e str
strip - divide uma string 
join - une uma string
"""

frase = '  olha só que , coisa interessante'
lista_frases_cruas= frase.split(',')

lista_frases = []
for i, frase in enumerate(lista_frases_cruas):
    lista_frases.append(lista_frases_cruas[i].strip())

# print(lista_frases_cruas)
# print(lista_frases)

frases_unidadas = ', '.join(lista_frases)
print(frases_unidadas)