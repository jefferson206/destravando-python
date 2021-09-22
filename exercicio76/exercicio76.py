from listaExercicio.uteis.util import Util
import time

def main():
    Util().enunciado('CRIE DOIS DICIONÁRIOS DIFERENTES E CONCATENE PARA CRIAR UM NOVO.')

    dicionario = {'nome': 'Jefferson'}
    segundoDicionario = {'idade': 31}

    dicionarioConcatenado = {}
    dicionarioConcatenado.update(dicionario)
    dicionarioConcatenado.update(segundoDicionario)

    print('Dicionario 1:', dicionario)
    print('Dicionario 2:', segundoDicionario)
    print('Dicionario concatenado:', dicionarioConcatenado)


if __name__ == '__main__':
    main()
