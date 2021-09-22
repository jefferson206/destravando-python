from listaExercicio.uteis.util import Util


def main():
    Util().enunciado('FAÇA UMA FUNÇÃO QUE RECEBA DOIS NÚMEROS E RETORNE QUAL DELES É O MAIOR')

    try:
        primeiro = float(input('Digite 1º valor: ').replace(',', '.'))
        segundo = float(input('Digite 2º valor: ').replace(',', '.'))
        maior = validaSePositivoOuNegativo(primeiro, segundo)
        print('Maior valor digitado: ', maior)
    except:
        print('Só pode ser valores numericos')


def validaSePositivoOuNegativo(primeiro, segundo):
    return max(primeiro, segundo)


if __name__ == '__main__':
    main()
