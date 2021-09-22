from listaExercicio.uteis.util import Util
import time


def main():
    Util().enunciado('ESCREVA UM PROGRAMA PARA MULTIPLICAR TODOS OS ITENS EM UM DICIONÁRIO.')

    dicionario = {
        'nota1': 10,
        'nota2': 8,
        'nota3': 7,
        'nota4': 8
    }
    multiplicacao = 1

    for chave in dicionario:
        multiplicacao *= dicionario[chave]

    print('Valores multiplicados:', multiplicacao)

if __name__ == '__main__':
    main()
