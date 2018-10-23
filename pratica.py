class Autor():
    def __init__(self, primeiro_nome, nascimento, ultimo_nome = '', meio_nome = None):
        self.primeiro_nome = primeiro_nome
        self.meio_nome = meio_nome
        self.ultimo_nome = ultimo_nome
        self.nascimento = nascimento

    def nome_como_citado(self):
        return '{} {}.'.format(self.ultimo_nome.upper(), self.primeiro_nome[0])

    def __str__(self):
        return 'Autor: {} {} {}'.format(self.primeiro_nome, self.ultimo_nome, self.nascimento)

class Livro():
    def __init__(self, titulo, ano, autores=[]):
        self.titulo = titulo
        self.ano = ano
        self.autores = autores

    @property
    def titulo(self):
        return self._titulo

    @titulo.setter
    def titulo(self, val):
        if not val:
            raise ValueError("Erro: não é possível um livro sem autor")
        self._titulo = val

    def __str__(self):
        return '{} - {}'.format(self.titulo, self.ano)

class Biblioteca():
    def __init__(self, livros):
        self.livros = livros

    def livros_por_autor(self):
        livros_autor = {}
        for livro in self.livros:
            for autor in livro.autores:
                if autor.nome_como_citado() not in livros_autor:
                    livros_autor[autor.nome_como_citado()] = [livro.__str__()]
                else:
                    livros_autor[autor.nome_como_citado()].append(livro.__str__())
        return livros_autor


    def __str__(self):
        return 'Livros{}'.format(self.livros)


if __name__ == "__main__":
    autor1 = Autor(primeiro_nome = 'Samuel', nascimento = '23/06/94', ultimo_nome = 'Cury')
    autor2 = Autor(primeiro_nome = 'Pedro', nascimento = '23/06/94', ultimo_nome = 'Pereira')
    autor3 = Autor(primeiro_nome = 'João', nascimento = '23/06/94', ultimo_nome = 'Silva')

    livro1 = Livro('As Crônicas', 1999, [autor1, autor2])
    livro2 = Livro('A Bola Quadrada de João', 2000, [autor1, autor3])
    livro3 = Livro('As Pedras de Pedro', 2001, [autor2])
    # livro4 = Livro(titulo = None, ano = 2001)  # teste livro sem titulo

    biblioteca = Biblioteca([livro1, livro2, livro3])

    print(biblioteca.livros_por_autor())
