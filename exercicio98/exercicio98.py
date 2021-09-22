from listaExercicio.uteis.util import Util


def main():
    Util().enunciado('ESCREVA UM PROGRAMA PARA IMPRIMIR OS NÚMEROS PARES DE UMA DETERMINADA LISTA.')

    lista = [12, 42, 52, 12, 55, 64, 7, 14, 15]

    imprimeValoresPares(lista)

def imprimeValoresPares(lista):
    for elemento in lista:
        if not elemento % 2:
            print(elemento)


if __name__ == '__main__':
    main()
