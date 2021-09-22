from listaExercicio.uteis.util import Util
import time

def main():
    Util().enunciado('LEIA UM NÚMERO INTEIRO E MOSTRE O CUBO ATÉ ESSE NÚMERO.')

    valor = int(input('Digite um valor: '))

    for contador in range(0, valor+1):
        print('O cubo de {} é: {}'.format(contador, contador**3))



if __name__ == '__main__':
    main()
