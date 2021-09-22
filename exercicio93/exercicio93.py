from listaExercicio.uteis.util import Util
from math import pi


def main():
    Util().enunciado('ESCREVA UMA FUNÇÃO QUE RECEBE UM NÚMERO REAL COMO ARGUMENTO E RETORNA O VALOR ABSOLUTO DESSE NÚMERO.')

    valor = float(input('Digite um valor qualquer: ').replace(',', '.'))

    print('\nValor Absoluto:', arredondamento(valor))


def arredondamento(valor):
    return abs(valor)


if __name__ == '__main__':
    main()
