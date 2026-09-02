# ===== HERANÇA =====
# _Fornecedor é a SUPERCLASSE (classe base/mãe).
# Ela concentra os atributos e comportamentos comuns a QUALQUER fornecedor,
# evitando repetição de código nas classes filhas.

class _Fornecedor:

    def __init__(self, nome, telefone, endereco):
        self.nome = nome
        self.telefone = telefone
        self.endereco = endereco

    # Método "genérico" que existe na superclasse.
    # Ele será SOBRESCRITO (override) pelas subclasses -> isso é polimorfismo.
    def exibir_informacoes(self):
        return f'{self.nome}'


# FornecedorFisico HERDA de _Fornecedor: ganha nome, telefone e endereco
# automaticamente, sem precisar reescrever esses atributos.
class FornecedorFisico(_Fornecedor):
    
    def __init__(self, nome, telefone, endereco, cpf):
        # super().__init__(...) chama o construtor da SUPERCLASSE
        # para reaproveitar a lógica de inicialização já existente.
        super().__init__(nome, telefone, endereco)
        self.cpf = cpf # atributo EXCLUSIVO desta subclasse

    # ===== POLIMORFISMO (sobrescrita de método) =====
    # Mesmo nome de método (informacoes) da superclasse,
    # mas com um COMPORTAMENTO DIFERENTE e específico da subclasse.
    def exibir_informacoes(self):
        return f'{self.nome} - {self.cpf}'


# FornecedorJuridico também HERDA de _Fornecedor.
class FornecedorJuridico(_Fornecedor):
    def __init__(self, nome, telefone, endereco, cnpj):
        super().__init__(nome, telefone, endereco)
        self.cnpj = cnpj # atributo EXCLUSIVO desta subclasse

    # Repare: essa classe NÃO sobrescreveu "informacoes".
    # Então, quando chamada, ela usa a versão da SUPERCLASSE (_Fornecedor).
    # Isso mostra que a sobrescrita é opcional: cada subclasse decide
    # se quer personalizar o comportamento herdado ou não.


fornecedor1 = FornecedorFisico('Maria S/A', '8699876546', 'Rua Principal, 2', '876543212300')

# POLIMORFISMO em ação: mesmo método "informacoes()" chamado da mesma forma,
# mas o resultado depende do TIPO REAL do objeto (aqui, FornecedorFisico).
print(fornecedor1.exibir_informacoes())
# saída: Maria S/A - 876543212300


# super(FornecedorFisico, fornecedor1) força o Python a "subir" na hierarquia
# e chamar o método informacoes() da SUPERCLASSE diretamente,
# ignorando a sobrescrita feita em FornecedorFisico.
print(super(FornecedorFisico, fornecedor1).exibir_informacoes())
# saída: Maria S/A

