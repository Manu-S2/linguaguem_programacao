class Aluno:

    def __init__(self, nome, matricula, prova_1, prova_2, trabalho):

        self.nome = nome
        self.matricula = matricula
        self.prova_1 = prova_1
        self.prova_2 = prova_2
        self.trabalho = trabalho

        self.media = float((2.5 * prova_1) + (2.5 * prova_2) + (2 * trabalho) / 2.5 + 2.5 + 2)


    def calculo():
        if self.media => 4.0 and self.media < 7.0:
            return True 
        else:
            return False


#tem que concertar tá errado !!!!!