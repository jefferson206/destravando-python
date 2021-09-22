from listaExercicio.uteis.util import Util
import time

def main():
    Util().enunciado('ESCREVA UM PROGRAMA PARA CONVERTER UMA LISTA EM UMA TUPLA.')

    lista = [1, 2, 3, 5, 5, 9, 9, 23, 28]


    print('Tipo: {} \nLista: {}'.format(type(lista), lista))

    tupla = tuple(lista)
    print('\nConvertendo....\n')
    time.sleep(1)
    print('Tipo: {} \nLista: {}'.format(type(tupla), tupla))



if __name__ == '__main__':
    main()
