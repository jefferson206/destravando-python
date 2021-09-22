from listaExercicio.uteis.util import Util


def main():
    Util().enunciado('ESCREVA UMA FUNÇÃO PARA CRIAR E IMPRIMIR UMA LISTA ONDE OS VALORES SÃO QUADRADOS DE NÚMEROS ENTRE 1 E 30 (AMBOS INCLUÍDOS).')

    imprimeValoresPares()


def imprimeValoresPares():
    lista = []
    for elemento in range(1, 31):
        lista.append(pow(elemento, 2))
    print('Lista:', lista)


if __name__ == '__main__':
    main()
