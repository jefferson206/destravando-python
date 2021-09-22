from listaExercicio.uteis.util import Util
import time

def main():
    Util().enunciado('FAÇA UM PROGRAMA QUE CALCULE E MOSTRE A SOMA DOS 50 PRIMEIROS NUMEROS PARES.')

    soma = 0
    for contador in range(0, 51):
        if contador % 2 == 0:
            soma += contador

    print('A soma de 0 até 50 dos valores pares é de:', soma)

if __name__ == '__main__':
    main()
