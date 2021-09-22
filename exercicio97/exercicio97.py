from listaExercicio.uteis.util import Util
from math import pi


def main():
    Util().enunciado('ESCREVA UMA FUNÇÃO PARA VERIFICAR SE UM NÚMERO ESTÁ EM UM DETERMINADO INTERVALO.')

    valor = float(input('Digite um valor: ').replace(',', '.'))

    verificaSeValorEstaEmIntervalo(valor)

def verificaSeValorEstaEmIntervalo(valor):
    if 0 <= valor <= 500:
        print('valor esta entre 0 e 500')
    else:
        print('valor NÃO esta entre 0 e 500...')


if __name__ == '__main__':
    main()
