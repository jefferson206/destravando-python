import math
from listaExercicio.uteis.util import Util


def main():
    Util().enunciadoEmDuasPartes(
        'LER UM NÚMERO INTEIRO. SE O NÚMERO LIDO FOR NEGATIVO, ESCREVA A MENSAGEM “ NÚMERO  INVÁLIDO”.',
        'SE O NÚMERO FOR POSITIVO, CALCULAR O LOGARITMO  DESTE  NUMERO.', 120)

    valor = float(input(f'Digite um numero: ').replace(',', '.'))

    if valor >= 0:
        print('O logaritmo de {} na base 10 é de: {} '.format(valor, round(math.log(valor, 10), 4)))
    else:
        print('O Valor deve ser maior positivo')


if __name__ == '__main__':
    main()
