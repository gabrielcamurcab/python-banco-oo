import random
import time
import banco
import auxiliar

print('Seja bem-vindo ao banco')
print('Abra sua conta...')
nome = input('Digite seu nome: ')
num = random.randint(100000, 999999)
print('Criando conta...')
time.sleep(2)
conta = banco.Conta(nome, num)
print(f'Conta criada!\nSeu nome: {nome}\nNúmero de sua conta: {num}')
time.sleep(2)
opcao = '5'

while opcao != '0':
    print('\n1 - Consultar saldo\n2 - Depositar\n3 - Sacar\n4 - Ver seu nome\n5 - Alterar seu nome\n0 - Sair')
    opcao = input('Digite a opção: ')
    auxiliar.switch_case(opcao)

print('Encerrando sistema bancário...')
time.sleep(2)
print('Sistema encerrado! Obrigado pela confiança!')