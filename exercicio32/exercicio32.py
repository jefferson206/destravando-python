from listaExercicio.uteis.util import Util


def main():
    Util().enunciado('ESCREVA UM ALGORITMO QUE LEIA UM NÚMERO E EXIBA SEU SUCESSOR.')

    valor = int(input(f'Digite um valor inteiro: '))

    print('Seu sucessor é:', valor+1)



if __name__ == '__main__':
    main()
