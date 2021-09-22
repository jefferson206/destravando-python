from listaExercicio.uteis.util import Util


def main():
    Util().enunciado('ESCREVA UM PROGRAMA PARA DETECTAR O NÚMERO DE VARIÁVEIS LOCAIS DECLARADAS EM UMA FUNÇÃO.')

    print('Quantidade de variaveis na função:', funcaoComVariaveisLocais.__code__.co_nlocals)

def funcaoComVariaveisLocais():
    nome = 'Jefferson'
    idade = 31
    caracteristicas = ['lindo']

if __name__ == '__main__':
    main()
