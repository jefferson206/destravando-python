from listaExercicio.uteis.util import Util
import time


def main():
    Util().enunciado('ESCREVA UM PROGRAMA PARA ITERAR SOBRE DICIONÁRIOS USANDO LOOPS FOR.')

    dicionario = {
        'nome': 'Jefferson',
        'idade': 31,
        'cor': 'branca'
    }

    for chave in dicionario:
        print(dicionario[chave])

if __name__ == '__main__':
    main()
