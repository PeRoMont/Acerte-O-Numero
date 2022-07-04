#Biblioteca
from random import randint #Biblioteca para gerar o número do computador

#Variavel
tentativas = 0 #Variavel para contar as tentativas

numpc = randint(1, 20) #Gerar o valor do computador
print('=' * 31)
print('ADIVINHE O NÚMERO DO COMPUTADOR')
print('=' * 31)
print('Computador: estou pensando em um número entre 1 e 20! Você consegue adivinhar qual é?')
numuser = int(input('Insira o número que o computador está pensando: ')) #Inserir o valor que o computador está pensando
tentativas += 1

while True:
    if numuser > numpc:
        print('Você digitou um número muito alto! Tente colocar um valor mais baixo.')
        numuser = int(input('Insira o valor novamente: ')) #Inserir o valor novamente
        tentativas += 1 #Contador de tentativas

    elif numuser < numpc:
        print('Você digitou um número muito baixo! Tente novamente inserindo um número mais alto.')
        numuser = int(input('Insira o número novamente: ')) #Inserir o valor novamente
        tentativas += 1 #Contador de tentativas

    else:
        print(f'PARABÉNS! VOCÊ DIGITOU {numuser} E O COMPUTADOR TAMBÉM PENSOU NO {numpc}')
        print(f'Você teve um total de {tentativas} tentativas.')
        break #A partir do momento que você acertar o programa PARA
