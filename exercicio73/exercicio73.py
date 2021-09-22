from listaExercicio.uteis.util import Util


def main():
    Util().enunciado('ESCREVA UM PROGRAMA PARA ENCONTRAR OS ITENS REPETIDOS DE UMA TUPLA')

    tupla = (1, 2, 3, 5, 5, 9, 9, 23, 28)

    lista = list(set(tupla))
    print('Tipo: {} \nTupla: {}'.format(type(tupla), tupla))

    tupla = tuple(lista)
    print('\nTupla com valores unicos', tupla)


if __name__ == '__main__':
    main()
