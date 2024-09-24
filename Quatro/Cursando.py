from Aluno import Aluno

class Cursando(Aluno):
    def __init__(self, matricula, nome, curso, ano_atual, ano_concluir):
        super().__init__(matricula, nome, curso)
        self.ano_atual = ano_atual
        self.ano_concluir = ano_concluir

    def get_ano_atual(self):
        return self.ano_atual

    def get_ano_concluir(self):
        return self.ano_concluir

    def set_ano_atual(self, ano_atual):
        self.ano_atual = ano_atual
        return "SUCESSO"

    def set_ano_concluir(self, ano_concluir):
        self.ano_concluir = ano_concluir
        return "SUCESSO"