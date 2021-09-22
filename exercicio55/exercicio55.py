from listaExercicio.uteis.util import Util
import time

def main():
    Util().enunciado('EXIBIR NÚMEROS DE -10 A -1 USANDO O LOOP FOR EXIBIR UMA MENSAGEM " FEITOOOO" APÓS A EXECUÇÃO BEM-SUCEDIDA DO LOOP FOR')

    for contador in range(-10, 0):
        time.sleep(0.3)
        print(contador, end='  ')

    print('\nFEITOOOO')


if __name__ == '__main__':
    main()
