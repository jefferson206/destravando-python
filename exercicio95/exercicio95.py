from listaExercicio.uteis.util import Util
from math import pi


def main():
    Util().enunciado('ESCREVA UMA FUNÇÃO PARA SOMAR TODOS OS NÚMEROS EM UMA LISTA.')

    lista = [12, 42, 52, 12, 55, 64]

    print('\nResultado:', somaDaLista(lista))


def somaDaLista(lista):
    soma = 0
    for elementos in lista:
        soma += elementos
    return soma

if __name__ == '__main__':
    main()
