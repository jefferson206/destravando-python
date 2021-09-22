from listaExercicio.uteis.util import Util

def main():
    Util().enunciado('PEÇA AO USUÁRIO PARA DIGITAR TRÊS VALORES INTEIROS E IMPRIMA A SOMA DELES.')
    soma = 0

    for indice in range(0, 3):
        valor = int(input(f'Digite o {indice+1}º valor inteiro: '))
        soma += valor

    print('\nA soma dos valores é de: ', soma)

if __name__ == '__main__':
    main()