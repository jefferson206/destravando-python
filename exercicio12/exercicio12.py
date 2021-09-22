from listaExercicio.uteis.util import Util

def main():
    Util().enunciado('LEIA UM NÚMERO INTEIRO E IMPRIMA O SEU ANTECESSOR E O SEU SUCESSOR.')

    valor = int(input(f'Digite um numero inteiro: '))

    print('\nNumero digitado: {} e seu antecessor é: {} e seu sucessor é: {} '.format(valor, valor-1, valor+1))

if __name__ == '__main__':
    main()