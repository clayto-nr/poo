from typing import List

class Venda:
    def __init__(self, dataVenda):
        self._produtos = []
        self._dataVenda = dataVenda
        self._total = 0.0

    def get_produtos(self):
        return self._produtos

    def get_dataVenda(self):
        return self._dataVenda

    def get_total(self):
        return self._total

    def set_produtos(self, produtos):
        self._produtos = produtos

    def set_dataVenda(self, dataVenda):
        self._dataVenda = dataVenda

    def set_total(self, total):
        self._total = total

    def calcularTotal(self):
        self._total = sum(produto.get_preco() * produto.get_quantidade() for produto in self._produtos)
        return self._total

    def adicionar_produto(self, produto):
        self._produtos.append(produto)
        self.calcularTotal()

    def remover_produto(self, nome_produto):
        for produto in self._produtos:
            if produto.get_nome() == nome_produto:
                self._produtos.remove(produto)
                self.calcularTotal()
                return True
        return False

    def listar_produtos(self):
        return [(produto.get_nome(), produto.get_preco(), produto.get_quantidade()) for produto in self._produtos]