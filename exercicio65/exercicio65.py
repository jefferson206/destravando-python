from listaExercicio.uteis.util import Util
import time

def main():
    Util().enunciado('ESCREVA UM PROGRAMA PARA OBTER O MENOR NÚMERO DE UMA LISTA.')

    valores = [1, 2, 2, 3, 5, 7, 10, 8, 5]

    print('Menor numero da lista:', min(valores))


if __name__ == '__main__':
    main()
