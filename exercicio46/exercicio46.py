from listaExercicio.uteis.util import Util


def main():
    Util().enunciado('FAÇA UM PROGRAMA QUE DETERMINE O MOSTRE OS CINCO PRIMEIROS MÚLTIPLOS DE 3, CONSIDERANDO NÚMEROS MAIORES QUE 0.')

    for multiploDeTres in range(3, 16, 3):
        print(multiploDeTres)


if __name__ == '__main__':
    main()
