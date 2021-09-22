from listaExercicio.uteis.util import Util


def main():
    Util().enunciado('ESCREVA UMA FUNÇÃO E QUANDO FOR USÁ-LA CHAME POR UM NOVO NOME.')

    dummy()
    novoNome = dummy
    novoNome()
    novoNome()
    novoNome()


def dummy():
    print('Chamada de função dummy')

if __name__ == '__main__':
    main()
