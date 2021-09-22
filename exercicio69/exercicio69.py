from listaExercicio.uteis.util import Util

def main():
    Util().enunciado('ESCREVA UM PROGRAMA PARA CRIAR UMA TUPLA COM DIFERENTES TIPOS DE DADOS.')

    tupla = (1, 2, 'a', 'b', ['Joao', 'Pedro'])

    print('Tipo: {} \nTupla: {}'.format(type(tupla), tupla))

if __name__ == '__main__':
    main()
