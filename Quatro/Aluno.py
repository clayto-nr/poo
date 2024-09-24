class Aluno:
    def __init__(self, matricula, nome, curso):
        self.matricula = matricula
        self.nome = nome
        self.curso = curso

    def get_matricula(self):
        return self.matricula

    def get_nome(self):
        return self.nome

    def get_curso(self):
        return self.curso
    
    def set_matricula(self, matricula):
        self.matricula = matricula
        return "SUCESSO"
  
    def set_nome(self, nome):
        self.nome = nome
        return "SUCESSO"

    def set_curso(self, curso):
        self.curso = curso
        return "SUCESSO"
    