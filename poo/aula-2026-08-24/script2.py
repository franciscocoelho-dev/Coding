class Produto:
    """
    Representa um produto de estoque, com descrição, quantidade e valor.
    A quantidade é controlada por meio de uma property, o que permite
    validar os valores antes de alterá-la (por exemplo, impedindo
    quantidades negativas).
    """

    def __init__(self, descricao: str) -> None:
        """
        Cria um novo produto.
        Argumento:
            descricao (str): nome/descrição do produto.

        O atributo _quantidade começa com um underscore porque é um
        atributo "protegido" — a ideia é que ele não seja acessado
        diretamente de fora da classe, e sim através da property
        'quantidade' (definida abaixo).
        """
        self.descricao: str = descricao
        self._quantidade: int = 0
        self.valor: float = 0


    @property
    def quantidade(self):
        """
        Permite LER o valor de _quantidade como se fosse um atributo comum.

        Graças ao decorador @property, é possível escrever:  p1.quantidade
        em vez de:
            p1.quantidade()  # chamada de método
        ou
            p1._quantidade   # acesso direto ao atributo protegido
        Returns:
            int: a quantidade atual em estoque.
        """
        return self._quantidade


    @quantidade.setter
    def quantidade(self, quant):
        """
        Permite ESCREVER um novo valor para _quantidade, mas de forma
        controlada — ou seja, com validação.

        Esse método é chamado automaticamente sempre que se faz:
            p1.quantidade = algum_valor

        Note que a operação é de SOMA (+=), e não de substituição:
        cada atribuição adiciona ao estoque existente, em vez de
        sobrescrevê-lo.

        Argumento:
            quant (int): quantidade a ser adicionada ao estoque.
                Só é aceita se for maior que zero; valores negativos
                ou iguais a zero são silenciosamente ignorados.
        """
        print('Passei no setter de quantidade')
        if quant > 0:
            self._quantidade += quant


p1 = Produto('Mouse')
# Isso NÃO é uma chamada de método comum: é a sintaxe de atribuição
# de atributo (p1.quantidade = 10) que, por baixo dos panos, aciona
# o método decorado com @quantidade.setter.
p1.quantidade = 10

# Como o setter usa +=, essa segunda atribuição SOMA 90 ao valor
# que já existia (10), resultando em 100 — e não em 90.
p1.quantidade = 90

# Aqui, p1.quantidade aciona o método decorado com @property,
# retornando o valor atual de _quantidade.
print(p1.quantidade)

