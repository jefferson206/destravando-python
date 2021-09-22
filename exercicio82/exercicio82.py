from listaExercicio.uteis.util import Util


def main():
    Util().enunciado('ESCREVA UMA FUNÇÃO DE FORMA QUE ELA POSSA ACEITAR UM TAMANHO VARIÁVEL DE ARGUMENTO E IMPRIMIR TODOS OS VALORES DOS ARGUMENTOS.')

    funcaoComArgumentosDinamicos('Jefferson', 31, 'lindo')


def funcaoComArgumentosDinamicos(*args):
    print('Quantidade de argumentos passados:', len(args))
    for variavel in args:
        print("Variavel:", variavel)

if __name__ == '__main__':
    main()
