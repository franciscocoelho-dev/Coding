class Fila:
    """
    Representa uma fila de pessoas (por exemplo, fila de supermercado,
    de loteria, de banco, etc).
    Cada objeto criado a partir dessa classe possui sua PRÓPRIA lista
    de pessoas, independente de outras filas que existam no programa.
    """

    def __init__(self):
        """
        Método construtor, chamado automaticamente quando um novo
        objeto Fila é criado (ex: Fila()).
        Inicializa a lista de pessoas vazia. Cada instância de Fila
        terá sua própria lista, guardada no atributo 'lista_pessoas'.
        """
        self.lista_pessoas = []

    def entrar_fila(self, nome):
        """
        Adiciona uma pessoa ao final da fila.
        Argumento --> nome (str): o nome da pessoa que está entrando na fila.
        """
        self.lista_pessoas.append(nome)

    def exibir_fila(self):
        """
        Retorna a lista de pessoas que estão atualmente na fila,
        na ordem em que entraram.
        Returns. -->  list: lista com os nomes das pessoas na fila.
        """
        return self.lista_pessoas


# Cria uma fila para o supermercado.
# Nesse momento, o __init__ é chamado automaticamente,
# criando uma lista vazia própria para essa fila.
supermercado = Fila()
supermercado.entrar_fila('Felipe')
supermercado.entrar_fila('Ana')


# Cria uma SEGUNDA fila, totalmente independente da primeira.
# Mesmo sendo da mesma classe Fila, cada objeto tem sua própria
# lista_pessoas — por isso Pedro não aparece na fila do supermercado.
loteria = Fila()
loteria.entrar_fila('Pedro')


print('Supermercado', supermercado.exibir_fila())
print('Loteria', loteria.exibir_fila())