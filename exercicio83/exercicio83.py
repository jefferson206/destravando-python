from listaExercicio.uteis.util import Util


def main():
    Util().enunciadoEmDuasPartes('ESCREVA UMA FUNÇÃO() QUE POSSA ACEITAR DUAS VARIÁVEIS E CALCULE A ADIÇÃO E SUBTRAÇÃO DELAS.',
                                 'E DEVE RETORNAR ADIÇÃO E SUBTRAÇÃO EM UMA ÚNICA CHAMADA DE RETORNE')

    somaSubtracao(40, 10)


def somaSubtracao(primeiro, segundo):
    subtracao, soma = (primeiro - segundo), (primeiro + segundo)

    print('Soma: {} \nSubtração: {}'.format(soma, subtracao))

if __name__ == '__main__':
    main()
