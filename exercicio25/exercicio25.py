from listaExercicio.uteis.util import Util


def main():
    Util().enunciado('FAÇA UM PROGRAMA QUE RECEBA DOIS NUMEROS E MOSTRE O MAIOR. SE POR ACASO, OS DOIS NÚMEROS FOREM IGUAIS, IMPRIMA A MENSAGEM NÚMEROS IGUAIS.')


    valorUm = float(input(f'Digite o primeiro numero: ').replace(',', '.'))
    valorDois = float(input(f'Digite o segundo numero: ').replace(',', '.'))

    if valorUm == valorDois:
        print('Os numeros são iguais')
        return
    print('O maior numero é', max(valorUm, valorDois))


if __name__ == '__main__':
    main()
