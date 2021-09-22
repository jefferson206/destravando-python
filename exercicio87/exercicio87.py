from listaExercicio.uteis.util import Util


def main():
    Util().enunciado('CRIE UMA FUNÇÃO QUE RECEBE COMO PARÂMETRO UM NÚMERO INTEIRO E DEVOLVE O SEU DOBRO.')

    valor = float(input('Digite um valor: '))
    dobro = valorDobrado(valor)
    print('\nDobro de {} é {}'.format(valor, dobro))


def valorDobrado(valor):
    return float(valor*2)


if __name__ == '__main__':
    main()
