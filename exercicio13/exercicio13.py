from listaExercicio.uteis.util import Util

def main():
    Util().enunciado('LEIA UM NÚMERO INTEIRO E IMPRIMA A SOMA DO SUCESSOR DE SEU TRIPLO COM O ANTECESSOR DE SEU DOBRO')

    valor = int(input(f'Digite um numero inteiro: '))
    sucessor = (valor+1)*3
    antecessor = (valor-1)*2

    print('\nNumero digitado: {} e seu antecessor é: {} e seu sucessor é: {} '.format(valor, valor-1, valor+1))
    print('E a soma do anterior de seu dobro e o sucessor com seu triplo é de:', (sucessor + antecessor))

if __name__ == '__main__':
    main()