from listaExercicio.uteis.util import Util

def main():
    Util().enunciado('ESCREVA UM PROGRAMA PARA CRIAR UMA TUPLA.')

    tupla = (1, 2, 3, 5, 8)

    print('Tipo: {} \nTupla: {}'.format(type(tupla), tupla))

if __name__ == '__main__':
    main()
