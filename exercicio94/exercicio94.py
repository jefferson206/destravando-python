from listaExercicio.uteis.util import Util
from math import pi


def main():
    Util().enunciadoEmDuasPartes('ESCREVA UMA FUNÇÃO QUE RECEBA DOIS NÚMERO INTEIRO (N E P) COMO ARGUMENTO E RETORNA N ELEVADO A P',
                     'SE N FOR MAIOR QUE P , CASO CONTRÁRIO RETORNE A RAIZ QUADRADA DE N.')

    valor = int(input('Digite um valor qualquer: '))
    segundoValor = int(input('Digite um valor qualquer: '))

    print('\nResultado:', calculo(valor, segundoValor))


def calculo(valor, elevado):
    if(valor > elevado):
        return pow(valor, elevado)
    else:
        return pow(valor, 1 / 2)


if __name__ == '__main__':
    main()
