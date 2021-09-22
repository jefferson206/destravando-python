from listaExercicio.uteis.util import Util


def main():
    Util().enunciado('LEIA UM NÚMERO INTEIRO E IMPRIMA ATÉ O VALOR 0.')

    valor = int(input(f'Digite um valor: '))
    print(valor)

    while valor != 0:
        if valor < 0:
            valor = valor + 1
        else:
            valor = valor - 1
        print(valor)


if __name__ == '__main__':
    main()
