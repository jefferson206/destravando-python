from listaExercicio.uteis.util import Util


def main():
    Util().enunciado('ESCREVA UM PROGRAMA PARA ADICIONAR UM I TEM EM UMA TUPLA.')

    tupla = (1, 2, 3, 5, 8)

    print('Tipo: {} \nTupla: {}'.format(type(tupla), tupla))
    lista = list(tupla)

    valor = int(input('\nDigite um valor para adicionar na tupla: '))
    lista.append(valor)
    tupla = tuple(lista)

    print('\nTupla modificada:', tupla)


if __name__ == '__main__':
    main()
