from listaExercicio.uteis.util import Util
import time

def main():
    Util().enunciado('FAÇA UM PROGRAMA QUE LEIA UM NÚMERO INTEIRO N E DEPOIS IMPRIMA OS N PRIMEIROS NUMEROS NATURAIS ÍMPARES.')

    valor = int(input('Digite um valor: '))
    if valor % 2:
        valor += 2
    else:
        valor += 1

    for contador in (valor, valor+2, valor+4):
        print(contador)

if __name__ == '__main__':
    main()
