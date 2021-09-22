from listaExercicio.uteis.util import Util


def main():
    Util().enunciado('ESCREVA UM ALGORITMO QUE LEIA DOIS NÚMEROS E EXIBA-OS EM  ORDEM CRESCENTE.')

    primeiroValor = int(input(f'Digite o 1ª valor: '))
    segundoValor = int(input(f'Digite o 2ª valor: '))
    lista = [primeiroValor, segundoValor]
    lista.sort()
    print('Valores ordenados:', lista[0], '...',  lista[1])



if __name__ == '__main__':
    main()
