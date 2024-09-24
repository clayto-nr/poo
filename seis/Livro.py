class Livro:
    def __init__(self, titulo, autor, anoPublicacao):
        self.titulo = titulo
        self.autor = autor
        self.anoPublicacao = anoPublicacao

    def get_titulo(self):
        return self.titulo

    def set_titulo(self, titulo):
        self.titulo = titulo

    def get_autor(self):
        return self.autor

    def set_autor(self, autor):
        self.autor = autor

    def get_anoPublicacao(self):
        return self.anoPublicacao

    def set_anoPublicacao(self, anoPublicacao):
        self.anoPublicacao = anoPublicacao

    def exibirLivro(self):
        return f"Título: {self.titulo}, Autor: {self.autor.exibirAutor()}, Ano de Publicação: {self.anoPublicacao}"