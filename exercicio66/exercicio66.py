from listaExercicio.uteis.util import Util
import time

def main():
    Util().enunciado('ESCREVA UM PROGRAMA PARA COPIAR UMA LISTA PARA OUTRA.')

    valores = [1, 2, 2, 3, 5, 7, 10, 8, 5]
    lista = valores.copy()

    lista.append(99)

    print('1ª Lista:', valores)
    print('2ª Lista:', lista)


if __name__ == '__main__':
    main()
