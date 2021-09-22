from listaExercicio.uteis.util import Util


def main():
    Util().enunciado('CRIE UMA FUNÇÃO QUE ACEITA DOIS ARGUMENTOS (NOME E IDADE) E IMPRIMIR SEU VALOR.')

    nome = str(input('Digite seu nome: '))
    idade = int(input('Digite sua idade: '))
    pessoa(nome, idade)


def pessoa(nome, idade):
    print('\nOlá {} seja grato pelos seus {} anos de vida !!!'.format(nome, idade))

if __name__ == '__main__':
    main()
