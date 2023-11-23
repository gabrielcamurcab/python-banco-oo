import time
import banco

conta = banco.Conta('',0)

def consultar_saldo():
    print(conta.getSaldo())

def depositar():
    valor = float(input('Digite o valor a acrescentar: '))
    print('Adicionando valor...')
    time.sleep(2)
    print(conta.addSaldo(valor))

def sacar():
    valor = float(input('Digite o valor a sacar: '))
    print('Sacando valor...')
    time.sleep(2)
    print(conta.delSaldo(valor))

def ver_nome():
    print(conta.getCliente())

def alterar_nome():
    novo_nome = input('Digite o novo nome: ')
    print('Alterando nome...')
    time.sleep(2)
    print(conta.setCliente(novo_nome))

def switch_case(case):
    switch_dict = {
        '1': consultar_saldo,
        '2': depositar,
        '3': sacar,
        '4': ver_nome,
        '5': alterar_nome
    }

    opcao = switch_dict.get(case)
    if opcao:
        opcao()