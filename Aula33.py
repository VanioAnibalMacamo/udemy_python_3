"""
Faça um programa que peça ao usuário para digitar um número inteiro,
informe se este número é par ou ímpar. Caso o usuário não digite um número
inteiro, informe que não é um número inteiro.
"""

print(40 * '-')
print('             EXERCICIO 1')

numero = input('Digite um número: ')

try:
    numero_int = int(numero)
    if numero_int % 2 == 0:
        print(f'O Número de entrada {numero} é par')
    else:
        print(f'O Número de entrada {numero} é impar')
except:
     print("Não é um número Inteiro")


# if numero.isnumeric():
#     numero_int = int(numero)
#     if numero_int % 2 == 0:
#         print('Par')
#     else:
#         print('Impar')
# else:
#     print("Não é um número Inteiro")

"""
Faça um programa que pergunte a hora ao usuário e, baseando-se no horário 
descrito, exiba a saudação apropriada. Ex. 
Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23.
"""

print(40 * '-')
print('             EXERCICIO 2')

hora = input('Digite a hora: ')

try:
    hora_int = int(hora)

    if hora_int >= 0 and hora_int <= 11:
        print(f'Bom dia {hora}')
    elif hora_int >= 12 and hora_int <= 17:
        print(f'Boa tarde {hora}')
    elif hora_int >= 18 and hora_int <= 23:
        print(f'Boa noite {hora}')
    else:
        print(f'A hora {hora} não está no intervalo de (0 - 23)')
except:
    print(f'O valor {hora} Não é válido')

"""
Faça um programa que peça o primeiro nome do usuário. Se o nome tiver 4 letras ou 
menos escreva "Seu nome é curto"; se tiver entre 5 e 6 letras, escreva 
"Seu nome é normal"; maior que 6 escreva "Seu nome é muito grande". 
"""

print(40 * '-')
print('             EXERCICIO 3')


nome_user = input('Digite o nome do usuario: ')

tamanho_nome = int(len(nome_user))

if tamanho_nome != 0:
    if tamanho_nome <= 4:
        print(f'O nome {nome_user} é curto')
    elif tamanho_nome >= 5 and tamanho_nome <= 6:
        print(f'O nome {nome_user} é normal')
    else:
        print(f'O nome {nome_user} é muito grande')
else:
    print('O nome não pode ser vazio')