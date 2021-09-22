from listaExercicio.uteis.util import Util


def main():
    Util().enunciado('FAÇA UM ALGORITMO QUE LEIA OS VALORES A, B, C E IMPRIMA NA TELA SE A SOMA DE A + B É MENOR QUE C .')

    valorA = int(input('Digite o 1º valor: '))
    valorB = int(input('Digite o 2º valor: '))
    valorC = int(input('Digite o 3º valor: '))

    somaDosValoresAeB = valorA + valorB

    if somaDosValoresAeB < valorC:
        print('\nA soma de do 1º valor e do 2º valor é menor que o 3º valor')
    else:
        print('\nA soma dos dois primeiros valores é maior que o 3º valor')


if __name__ == '__main__':
    main()
