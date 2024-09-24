from Cursando import *

class Concluinte(Cursando):
    def __init__(self, matricula, nome, curso, ano_atual, ano_concluir, ano_conclusao, emitiu_certificado):
        super().__init__(matricula, nome, curso, ano_atual, ano_concluir)
        self.ano_conclusao = ano_conclusao
        self.emitiu_certificado = emitiu_certificado

    def mostrar_concluinte(self):
        print(f"MATRÍCULA: {self.get_matricula().upper()} 🎓")
        print(f"NOME: {self.get_nome().upper()} 📝")
        print(f"CURSO: {self.get_curso().upper()} 📚")
        print(f"ANO DE CONCLUSÃO: {str(self.ano_conclusao).upper()} 📅")
        print(f"CERTIFICADO EMITIDO: {str(self.emitiu_certificado).upper()} ✔️")


concluinte1 = Concluinte("19991041110028", "CESIMAR XAVIER", "INFORMATICO", "0000", "1111", "2222", "sim")
concluinte1.mostrar_concluinte()