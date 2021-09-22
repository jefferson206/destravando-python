from listaExercicio.uteis.util import Util
import time

def main():
    Util().enunciado('ESCREVA UM PROGRAMA PARA OBTER O MAIOR NÚMERO DE UMA LISTA.')

    valores = [1, 2, 2, 3, 5, 7, 10, 8, 5]

    print('Maior numero da lista:', max(valores))


if __name__ == '__main__':
    main()
