from listaExercicio.uteis.util import Util
import time

def main():
    Util().enunciado('IMPRIMIR TABUADA DE UM DETERMINADO NÚMERO.')

    multiplicar = int(input('Digite o valor que desejar ver a tabuada: '))

    valor = 1
    while valor <= 10:
        print('{} x {} = {}'.format(valor, multiplicar, (valor*multiplicar)))
        valor += 1


if __name__ == '__main__':
    main()
