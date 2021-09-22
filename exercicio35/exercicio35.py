from listaExercicio.uteis.util import Util


def main():
    Util().enunciado('FAÇA UM ALGORITMO QUE LEIA UMA VARIÁVEL E SOME 5 CASO SEJA PAR OU SOME 8 CASO SEJA ÍMPAR, IMPRIMIR O RESULTADO DESTA OPERAÇÃO.')

    valor = int(input('Digite o um valor: '))

    if valor % 2:
        print('Resultado: ', valor+8)
    else:
        print('Resultado: ', valor+5)


if __name__ == '__main__':
    main()
