"""
Faça uma lista de comprar com listas
O usuário deve ter a possibilidade de
inserir, apagar e listar valores da sua lista
Não permita que o programa quebre com 
erros de índices inexistentes na lista.
"""

lista = []

while True:
    print('Selecione uma opção')
    print('[i]nserir   [a]pagar  [l]istar')
    op = input(':')

    if(op == 'i'):
        valor = input('Digite um valor: ')
        lista.append(valor)
    elif (op == 'a'):
    
        indice = input('Digite o indice: ')
        if (int(indice) >= 0) and int(indice) <= len(lista)-1:
            del(lista[int(indice)])
        else:
             print('Indice invalido!')
    elif(op == 'l'):
        if len(lista) > 0:
            for indice, nome in enumerate(lista):
                print(indice, nome)
        else:
            print('Lista Vazia!')
    else:
        print('Opção Invalida!')



#Solução do Professor

# import os

# lista = []

# while True:
#     print('Selecione uma opção')
#     opcao = input('[i]nserir [a]pagar [l]istar: ')

#     if opcao == 'i':
#         os.system('clear')
#         valor = input('Valor: ')
#         lista.append(valor)
#     elif opcao == 'a':
#         indice_str = input(
#             'Escolha o índice para apagar: '
#         )

#         try:
#             indice = int(indice_str)
#             del lista[indice]
#         except ValueError:
#             print('Por favor digite número int.')
#         except IndexError:
#             print('Índice não existe na lista')
#         except Exception:
#             print('Erro desconhecido')
#     elif opcao == 'l':
#         os.system('clear')

#         if len(lista) == 0:
#             print('Nada para listar')

#         for i, valor in enumerate(lista):
#             print(i, valor)
#     else:
#         print('Por favor, escolha i, a ou l.')