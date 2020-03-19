class Pessoa:
    def cumprimentar(self):
        return f'Ola {id(self)}'


if __name__ == '__main__':
    p = Pessoa()
    print(Pessoa.cumprimentar(p))

    print(id(p))

    print(p.cumprimentar())     # nao precisa passar o proprio objeto no parâmetro self
    # print(p.cumprimentar(7))    # se passar qualquer parâmetro tem erro de 2 parâmetros
