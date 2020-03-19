class Pessoa:
    # o metodo __init__ inicializa os atributos de dados
    def __init__(self
                 ,*filhos
                 ,nome=None
                 ,idade=30
                 ):
        self.nome = nome
        self.idade = idade
        self.filhos = list(filhos)

    def cumprimentar(self):         # na criação com parâmetro já define o próprio objeto self.
        return f'Ola {id(self)}'    # verifica-se o mesmo objeto pelo id


if __name__ == '__main__':
    kazuo = Pessoa(nome='Kazuo')
    akira = Pessoa(nome='Akira')
    nelson = Pessoa(kazuo,akira, nome='Nelson')
    print(nelson.cumprimentar())
    print(nelson.nome)
    print(nelson.idade)
    for filho in nelson.filhos:
        print(filho.nome)
    nelson.sobrenome = 'Mizutani'
    del nelson.filhos
    print(nelson.__dict__)
    print(kazuo.__dict__)