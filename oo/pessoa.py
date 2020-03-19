class Pessoa:
    def cumprimentar(self):         # na criação com parâmetro já define o próprio objeto self.
        return f'Ola {id(self)}'    # verifica-se o mesmo objeto pelo id


if __name__ == '__main__':
    p = Pessoa()
    print(Pessoa.cumprimentar(p))

    print(id(p))

    print(p.cumprimentar())     # nao precisa passar o proprio objeto no parâmetro self
    # print(p.cumprimentar(7))    # se passar qualquer parâmetro tem erro de 2 parâmetros
