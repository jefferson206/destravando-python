from listaExercicio.uteis.util import Util
import time


def main():
    Util().enunciado('ESCREVA UM PROGRAMA PARA VERIFICAR SE UMA DETERMINADA CHAVE JÁ EXISTE EM UM DICIONÁRIO.')

    dicionario = {
        'nome': 'Jefferson',
        'idade': 31,
        'cor': 'branca'
    }
    print(type(dicionario))
    chave = str(input('Digite a chave que esta buscando o valor: '))

    checagemDeChaveNoDicionaio(dicionario, chave)


def checagemDeChaveNoDicionaio(dicionario, chave):
    if chave in dicionario:
        print('\nValor da chave {} é: {}'.format(chave, dicionario[chave]))
    else:
        print('\nOOOOOPS... Chave não encontrada no dicionario')


if __name__ == '__main__':
    main()
