class Produto:
    def __init__(self, nome, preco, quantidade):
        self._nome = nome
        self._preco = preco
        self._quantidade = quantidade

    def get_nome(self):
        return self._nome

    def get_preco(self):
        return self._preco

    def get_quantidade(self):
        return self._quantidade

    def set_nome(self, nome):
        self._nome = nome

    def set_preco(self, preco):
        self._preco = preco

    def set_quantidade(self, quantidade):
        self._quantidade = quantidade