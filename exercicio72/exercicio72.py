from listaExercicio.uteis.util import Util


def main():
    Util().enunciado('ESCREVA UM PROGRAMA PARA OBTER O 4 º ELEMENTO E O ÚLTIMO DE UMA TUPLA.')

    tupla = (1, 2, 3, 5, 8, 10, 18, 23, 28)

    print('Tipo: {} \nTupla: {}'.format(type(tupla), tupla))
    print('\n4º Elemento: ', tupla[3], '\nUltimo Elemento: ', tupla[len(tupla)-1])


if __name__ == '__main__':
    main()
