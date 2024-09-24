class Biblioteca:
    def __init__(self):
        self.livros = []

    def adicionarLivro(self, livro):
        self.livros.append(livro)

    def removerLivro(self, titulo):
        self.livros = [livro for livro in self.livros if livro.get_titulo() != titulo]

    def buscarLivro(self, titulo):
        for livro in self.livros:
            if livro.get_titulo() == titulo:
                return livro.exibirLivro()
        return "Livro não encontrado"

    def listarLivros(self):
        return [livro.exibirLivro() for livro in self.livros]