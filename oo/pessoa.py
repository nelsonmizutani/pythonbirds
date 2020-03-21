class Pessoa:
    olhos = 2

    # o metodo __init__ inicializa os atributos de dados
    def __init__(self, *filhos, nome=None, idade=30):
        self.nome = nome
        self.idade = idade
        self.filhos = list(filhos)

    def cumprimentar(self):
        return f'Ola, meu nome é {self.nome}'

    @staticmethod
    def metodo_estatico():
        return 'calculo'

    @classmethod
    def nome_e_atributos_de_classe(cls):
        return f'{cls} - olhos {cls.olhos}'

class Homem(Pessoa):
    def cumprimentar(self):
        # cumprimentar_da_classe=self.cumprimentar() # isto gera loop ao chamar ela mesma
        cumprimentar_da_classe = super().cumprimentar()
        return f' {cumprimentar_da_classe}. Aperto de mão'


class Mutante(Pessoa):
     olhos = 3

if __name__ == '__main__':
    akira = Homem(nome='Akira')
    kazuo = Mutante(nome='Kazuo')
    nelson = Homem(kazuo,akira, nome='Nelson')
    print(nelson.nome)
    print(nelson.idade)
    for filho in nelson.filhos:
        print(filho.nome)
    del nelson.filhos
    print(nelson.__dict__)
    print(kazuo.__dict__)
    print(Pessoa.olhos)     # referência direta na classe
    print(nelson.olhos)     # referência no objeto
    print(kazuo.olhos)     # referência no objeto
    print(nelson.cumprimentar())
    print(kazuo.cumprimentar())
