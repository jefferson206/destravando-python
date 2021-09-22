from listaExercicio.uteis.util import Util

def main():
    Util().enunciado('FAÇA UM PROGRAMA QUE LEIA UM NÚMERO INTEIRO E O IMPRIMA.')

    valor = int(input('Digite um valor inteiro: '))
    print('Valor digitado: ', valor)

if __name__ == '__main__':
    main()