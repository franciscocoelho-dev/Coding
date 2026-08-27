class ContaBancaria:
    """
    Representa uma conta bancária simples, com titular e saldo.

    Cada conta criada é independente das demais: possui seu próprio
    titular e seu próprio saldo, e pode interagir com outras contas
    (por exemplo, através de transferências).
    """


    def __init__(self, titular: str) -> None:
        """
        Cria uma nova conta bancária.
        Toda conta começa com saldo igual a 0.
        Argumento. -->  titular (str): nome da pessoa dona da conta.
        """
        self.titular = titular
        self.saldo = 0


    def consultar_saldo(self) -> float:
        """
        Consulta o saldo atual da conta.
        Returns  -->  float: o saldo disponível na conta.
        """
        return self.saldo


    def depositar(self, valor: float) -> bool:
        """
        Deposita um valor na conta, desde que seja positivo.
        Argumento  -->  valor (float): quantia a ser depositada.
        Returns:
            bool: True se o depósito foi realizado com sucesso,
                  False se o valor informado for inválido (menor ou
                  igual a zero).
        """
        if valor <= 0:
            return False
        self.saldo += valor
        return True


    def sacar(self, valor: float) -> bool:
        """
        Saca um valor da conta, se houver saldo suficiente.
        Argumento  -->  valor (float): quantia a ser sacada.
        Returns:
            bool: True se o saque foi realizado com sucesso,
                  False se o valor for inválido ou o saldo for
                  insuficiente.
        """
        if self.saldo >= valor and valor > 0:
            self.saldo -= valor
            return True
        return False


    def transferir(self, valor: float, conta_destino: 'ContaBancaria'):
        """
        Transfere um valor desta conta para outra conta.

        Internamente, a transferência é feita em duas etapas:
        primeiro é sacado o valor desta conta e, se o saque der certo,
        o mesmo valor é depositado na conta de destino.

        Argumentos:
            valor (float): quantia a ser transferida.
            conta_destino (ContaBancaria): conta que vai receber o valor.
                A string 'ContaBancaria' entre aspas é usada aqui porque,
                no momento em que a classe está sendo definida, ela
                ainda não existe "pronta" — essa é uma forma de indicar
                o tipo sem gerar erro (forward reference).

        Returns:
            bool: True se a transferência foi realizada com sucesso,
                  False caso o saque tenha falhado (saldo insuficiente
                  ou valor inválido).
        """
        if self.sacar(valor) == True:
            conta_destino.depositar(valor)
            return True
        return False




conta1 = ContaBancaria('Ana')
conta2 = ContaBancaria('João')


conta1.depositar(300)
print('Saldo C1: ', conta1.consultar_saldo())

conta2.depositar(100)
print('Saldo C2: ', conta2.consultar_saldo())


# transferir() usa sacar() e depositar() internamente:
# primeiro tenta sacar 50 de conta1; se der certo, deposita 50 em conta2.
conta1.transferir(50, conta2)
print('Saldo C1: ', conta1.consultar_saldo())
print('Saldo C2: ', conta2.consultar_saldo())

