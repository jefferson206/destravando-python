from listaExercicio.uteis.util import Util
import time


def main():
    Util().enunciado('ESCREVA UM PROGRAMA PARA REMOVER UMA CHAVE DE UM DICIONÁRIO')

    dicionario = {
        'nome': 'Jefferson',
        'idade': 31,
        'cor': 'branca'
    }
    print('Dicionario:', dicionario)

    chave = str(input('\nDigite a chave que deseja deletar: '))
    checagemDeChaveNoDicionaio(dicionario, chave)

    print('\nDicionario:', dicionario)

def checagemDeChaveNoDicionaio(dicionario, chave):
    if chave in dicionario:
        dicionario.pop(chave)
    else:
        print('\nOOOOOPS... Chave não encontrada no dicionario')

if __name__ == '__main__':
    main()
