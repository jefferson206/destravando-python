from listaExercicio.uteis.util import Util
import time

def main():
    Util().enunciado('FAÇA UM PROGRAMA QUE LEIA UM NÚMERO INTEIRO POSITIVO N E IMPRIMA TODOS OS NÚMEROS NATURAIS DE 0 ATÉ N EM ORDEM DECRESCENTE')

    valor = int(input('Digite um valor: '))
    if valor < 0:
        print('Valor deve ser positivo....')

    print(*reversed(range(valor+1)))


if __name__ == '__main__':
    main()
