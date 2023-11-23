class Conta:
    def __init__(self, nome, numero):
        self.cliente = nome
        self.num = numero
        self.saldo = 0.0
    
    def getSaldo(self):
        return self.saldo
    
    def getCliente(self):
        return self.cliente
    
    def setCliente(self, nome):
        self.cliente = nome
        return 'Nome alterado com sucesso!'
    
    def addSaldo(self, valor):
        self.saldo += valor
        return f'Você adicionou R$ {valor} à sua conta!'
    
    def delSaldo(self, valor):
        if(self.saldo >= valor):
            self.saldo -= valor
            return f'Você sacou R$ {valor} da sua conta!'
        else:
            return 'Você nãp tem saldo suficiente!'