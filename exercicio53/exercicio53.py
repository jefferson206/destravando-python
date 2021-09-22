from listaExercicio.uteis.util import Util
import time

def main():
    Util().enunciado('IMPRIMA OS PRIMEIROS 10 NÚMEROS NATURAIS USANDO O LOOP WHILE.')

    valor = 0
    while valor <= 10:
        print(valor)
        time.sleep(0.3)
        valor += 1


if __name__ == '__main__':
    main()
