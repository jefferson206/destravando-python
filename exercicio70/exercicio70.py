from listaExercicio.uteis.util import Util


def main():
    Util().enunciado('ESCREVA UM PROGRAMA PARA CRIAR UMA TUPLA COM NÚMEROS E IMPRIMIR UM ITEM')

    tupla = (1, 2, 3, 5, 8)

    print('Tipo: {} \nTupla: {}'.format(type(tupla), tupla))

    valor = int(input('\nDigite um valor de 0 a 4: '))
    if valor < 0 or valor > 4:
        print('Elemento não encontrado na tupla...')
        return
    print('Elemento da tupla:', tupla[valor])


if __name__ == '__main__':
    main()
