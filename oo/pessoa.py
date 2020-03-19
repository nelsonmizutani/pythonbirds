class Pessoa:
    def __init__(self, nome=None,
                 idade=50):  # o metodo __init__ inicializa os atributos de dados
        self.idade = idade
        self.nome = nome

    def cumprimentar(self):         # na criação com parâmetro já define o próprio objeto self.
        return f'Ola {id(self)}'    # verifica-se o mesmo objeto pelo id


if __name__ == '__main__':
    p = Pessoa('Nelson')
    print(Pessoa.cumprimentar(p))
    print(id(p))
    print(p.cumprimentar())
    print(p.nome)
    p.nome = 'Mizutani'
    print(p.nome)
    print(p.idade)
