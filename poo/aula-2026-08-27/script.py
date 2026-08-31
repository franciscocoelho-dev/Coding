from datetime import datetime

class ContaBancaria:
    def __init__(self, titular: 'Cliente'):
        self.titular = titular          # Associação: ContaBancaria "conhece" um Cliente,
                                        # mas não é responsável por criá-lo ou destruí-lo.
                                        # O Cliente existe de forma independente da conta.
        self.saldo = 0
        self.historico = Historico()    # Composição: Historico é criado aqui, dentro do
                                        # __init__, e pertence exclusivamente a esta conta.
                                        # Se a ContaBancaria for destruída, o Historico
                                        # também deixa de existir (não tem vida própria).

    def sacar(self, valor: float) -> bool:
        if self.saldo >= valor and valor > 0:
            self.saldo -= valor
            self.historico.inserir_historico(f'Saque de {valor} em {datetime.now()}')
            return True
        return False

    def ver_extrato(self):
        return self.historico.ver_historico()


class Cliente:
    def __init__(self, nome, cpf):
        self.nome = nome
        self.cpf = cpf


class Agencia:
    def __init__(self, numero: str):
        self.numero = numero
        self.contas = []                # Agregação: a lista guarda referências a objetos ContaBancaria
                                        # que foram criados fora da Agencia (no código cliente).
                                        # A Agencia "tem" contas, mas não é dona do ciclo de vida delas.

    def vincular_conta(self, conta: 'ContaBancaria'):
        self.contas.append(conta)       # Agregação: a conta já existia antes de ser vinculada;
                                        # a Agencia apenas passa a referenciá-la. Se a Agencia
                                        # for destruída, a ContaBancaria continua existindo.


class Historico:
    def __init__(self):
        self.lista_historico = []

    def inserir_historico(self, movimentacao):
        self.lista_historico.append(movimentacao)

    def ver_historico(self):
        return self.lista_historico


# --------------

'''
cliente1 = Cliente('Ana', '00000000000')
conta1 = ContaBancaria(cliente1)

cliente2 = Cliente('João', '11111111111')
conta2 = ContaBancaria(cliente2)

agencia1 = Agencia('0090-0')
agencia1.vincular_conta(conta1)
agencia1.vincular_conta(conta2)
'''

titular1 = Cliente('Pedro', '77766655544')  # Cliente criado de forma independente
conta1 = ContaBancaria(titular1)            # Associação em ação: passamos uma referência a um
                                            # objeto que já existe e continuaria existindo mesmo
                                            # se a conta fosse deletada.
conta1.saldo = 400
conta1.sacar(200)

print(conta1.ver_extrato())

