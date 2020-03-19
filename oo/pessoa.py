class Pessoa:
    olhos = 2

    # o metodo __init__ inicializa os atributos de dados
    def __init__(self, *filhos, nome=None, idade=30):
        self.nome = nome
        self.idade = idade
        self.filhos = list(filhos)

    def cumprimentar(self):  # na criação com parâmetro já define o próprio objeto self.
        return f'Ola {id(self)}'  # verifica-se o mesmo objeto pelo id

    @staticmethod
    def metodo_estatico():
        return 'calculo'

    @classmethod
    def nome_e_atributos_de_classe(cls):
        return f'{cls} - olhos {cls.olhos}'

if __name__ == '__main__':
    kazuo = Pessoa(nome='Kazuo')
    akira = Pessoa(nome='Akira')
    nelson = Pessoa(kazuo,akira, nome='Nelson')
    print(nelson.nome)
    print(nelson.idade)
    for filho in nelson.filhos:
        print(filho.nome)
    del nelson.filhos
    kazuo.olhos  = 1
    print(nelson.__dict__)
    print(kazuo.__dict__)
    print(Pessoa.olhos)     # referência direta na classe
    print(nelson.olhos)     # referência no objeto
    print(kazuo.olhos)     # referência no objeto
    print(id(Pessoa.olhos), id(kazuo.olhos))   # o id é o mesmo
    Pessoa.olhos = 3
    print(Pessoa.olhos)     # referência direta na classe
    print(Pessoa.metodo_estatico(), kazuo.metodo_estatico())
    print(Pessoa.nome_e_atributos_de_classe(), kazuo.nome_e_atributos_de_classe())

