"""
Faça um jogo para o usuário adivinhar qual
a palavra secreta.
- Você vai propor uma palavra secreta
qualquer e vai dar a possibilidade para
o usuário digitar apenas uma letra.
- Quando o usuário digitar uma letra, você 
vai conferir se a letra digitada está
na palavra secreta.
    - Se a letra digitada estiver na
    palavra secreta; exiba a letra;
    - Se a letra digitada não estiver
    na palavra secreta; exiba *.
Faça a contagem de tentativas do seu
usuário.
"""

# print(60 * '-')
# print(10*' ', 'JOGO DE ADVINHA DA PALAVRA SECRETA')

# palavra_secreta = 'Programar'
# palavra_formatada = (len(palavra_secreta) * '*')
# palavra_formatada = list(palavra_formatada) 

# count = 0

# while True:
    
#     letra_user = input('Digite uma letra:')
#     count +=1
#     if len(letra_user) == 1:
        
#         for letra in palavra_secreta:
#             if letra_user == letra:
#                print('existe')
#                palavra_formatada [palavra_secreta.index(letra)] = letra
#                palavra_formatada = "".join(palavra_formatada)
#                print("Palavra Formatada: "+palavra_formatada)
#                palavra_formatada = list(palavra_formatada) 
#     else:
#         print('Digite apenas uma letra')
    
#     if palavra_secreta == palavra_formatada:
#         break

# print('Numero de tentavivas: ', count)


import os

palavra_secreta = 'Programar'
letras_acertadas = ''
count = 0

while True:

    letra_digitada = input('Digite uma letra: ')

    count +=1

    if len(letra_digitada) > 1:
        print('Digite apenas uma letra.')
        continue
    
    if letra_digitada in palavra_secreta:
        letras_acertadas += letra_digitada
    
    palavra_formada = ''

    for letra_secreta in palavra_secreta:
        if letra_secreta in letras_acertadas:
           palavra_formada += letra_secreta
        else:
            palavra_formada += '*'

    print('Palavra formada: ',palavra_formada)

    if palavra_formada == palavra_secreta:
      os.system('cls')
      print('Você ganhou, parabens!')
      print('A palavra era ', palavra_formada)
      print('Tentativas: ', count)
      break


   




