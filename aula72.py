#EXERCICIOS COM FUNÇÕES

# Crie uma função que multiplica todos os argumentos não nomeados recebidos
#Retorna o total para uma variavel e mostre o valor da variavel

#Crie uma função que fala se um número é par ou impar 
#Retorna se o número é par ou impar

def multiplica(*args):
    valor = 1;
    for numero in args:
        valor *= numero
    
    return valor

def par_ou_impar(valor):
    
    if valor % 2 == 0:
        return 'PAR'
    
    return 'IMPAR'

print(multiplica(1,2,4))
print(par_ou_impar(3))