from listaExercicio.uteis.util import Util


def main():
    Util().enunciado('FAÇA UM PROGRAMA QUE RECEBA UM NÚMERO INTEIRO E VERIFIQUE SE ESTE NÚMERO É PAR OU ÍMPAR.')

    valor = float(input(f'Digite um numero qualquer: ').replace(',', '.'))

    if valor % 2:
        print('O numero {} é impar'.format(valor))
    else:
        print('O numero {} é par'.format(valor))


if __name__ == '__main__':
    main()
