from listaExercicio.uteis.util import Util
import time

def main():
    Util().enunciado('ESCREVA UM PROGRAMA PARA SOMAR TODOS OS I TENS EM UMA LISTA.')

    valores = [1, 2, 2, 3, 5, 7, 10, 8, 5]

    resultado = 0
    for valor in valores:
        resultado += valor

    print('Soma da lista:', resultado)


if __name__ == '__main__':
    main()
