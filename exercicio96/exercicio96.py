from listaExercicio.uteis.util import Util
from math import pi


def main():
    Util().enunciado('ESCREVA UMA FUNÇÃO PARA MULTIPLICAR TODOS OS NÚMEROS EM UMA LISTA.')

    lista = [12, 42, 52, 12, 55, 64]

    print('\nResultado:', multiplicaElementosDaLista(lista))


def multiplicaElementosDaLista(lista):
    multiplicacao = 1
    for elementos in lista:
        multiplicacao *= elementos
    return multiplicacao

if __name__ == '__main__':
    main()
