from listaExercicio.uteis.util import Util
import time

def main():
    Util().enunciado('ESCREVA UM PROGRAMA PARA ADICIONAR UMA CHAVE A UM DICIONÁRIO.')

    dicionario = {}

    print('Tipo:', type(dicionario), '\nValores:', dicionario)

    nome = str(input('\nDigite seu nome: '))

    dicionario['nome'] = nome
    print('\nTipo:', type(dicionario), '\nValores:', dicionario)

if __name__ == '__main__':
    main()
