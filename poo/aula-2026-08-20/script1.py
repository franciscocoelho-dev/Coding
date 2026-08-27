class Pessoa:
    """
    Classe que representa uma Pessoa.
    Por enquanto, essa classe possui apenas um método de exemplo,
    usado para demonstrar como funciona a chamada de métodos em Python.
    """


    def mostrar(self):
        """
        Exibe uma mensagem simples no console.
        O parâmetro 'self' é obrigatório em todo método de uma classe.
        Ele representa o próprio objeto que está chamando o método,
        e é através dele que o método pode acessar atributos e
        outros métodos da instância.
        """

        print('Estou no método mostrar')


# Cria uma instância (um objeto) da classe Pessoa.
p1 = Pessoa()

# Chama o método mostrar() usando o objeto p1.
# Note que não passamos nada para o parâmetro 'self':
# o próprio Python se encarrega de enviar p1 automaticamente.
p1.mostrar()


