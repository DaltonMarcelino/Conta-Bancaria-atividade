from datetime import datetime
import pytz

class ContaCorrente():

    @staticmethod
    def _data_hora():
        fuso_BR = pytz.timezone('Brazil/East')
        horario_BR = datetime.now(fuso_BR)
        return horario_BR

    def __init__(self, nome, cpf, agencia, num_conta):
        self.nome = nome
        self.cpf = cpf
        self.saldo = 0
        self.limite = None
        self.agencia = agencia
        self.num_conta = num_conta
        self.transacoes = []
          
# programa
conta_lira = ContaCorrente("Lira", "111.222.333-45")
print("Saldo da conta é: ", conta_lira.saldo)
print(conta_lira.cpf)

       
def consultar_saldo(self):
        print('Seu saldo atual é de R${:,.2f}'.format(self.saldo))
        pass
    
def depositar_dinheiro(self,valor):
        self.saldo += valor
        self.transacoes.append((valor, self.saldo, ContaCorrente._data_hora()))
        pass

def limite_conta(self):
        self.limite =-1000
        return self.limite

def sacar_dinheiro(self, valor):
        if self.saldo -valor < self.limite_conta():
            print('Você não tem saldo insuficiente')
            self.consultar_saldo()
        else:
            self.saldo -= valor
            self.transacoes.append((valor, self.saldo, ContaCorrente._data_hora()))
            pass

def consultar_historico_transacoes (self, transacoes):
    print('Histórico de Transacões:')
    for transacao in self.transacoes:
        print(transacao)




conta_lira = ContaCorrente("Lira", "111.222.333-45")
conta_lira.consultar_saldo()

#depositar um dinheirinho na conta:
conta_lira.depositar_dinheiro(10000)
conta_lira.consultar_saldo()

#acando um dinheirinho da conta:
conta_lira.sacar_dinheiro (1000000)
conta_lira.consultar_saldo()

print('Saldo Final: ')
conta_lira.consultar_saldo()