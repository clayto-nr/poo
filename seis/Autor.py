class Autor:
    def __init__(self, nome, nacionalidade, dataNascimento):
        self.nome = nome
        self.nacionalidade = nacionalidade
        self.dataNascimento = dataNascimento

    def get_nome(self):
        return self.nome

    def set_nome(self, nome):
        self.nome = nome

    def get_nacionalidade(self):
        return self.nacionalidade

    def set_nacionalidade(self, nacionalidade):
        self.nacionalidade = nacionalidade

    def get_dataNascimento(self):
        return self.dataNascimento

    def set_dataNascimento(self, dataNascimento):
        self.dataNascimento = dataNascimento

    def exibirAutor(self):
        return f"Nome: {self.nome}, Nacionalidade: {self.nacionalidade}, Data de Nascimento: {self.dataNascimento}"