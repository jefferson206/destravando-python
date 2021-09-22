from listaExercicio.uteis.util import Util

def main():
    Util().enunciado('FAÇA UM PROGRAMA QUE RECEBA DOIS NUMEROS E MOSTRE QUAL DELES É O MAIOR.')

    valorUm = float(input(f'Digite o primeiro numero: ').replace(',', '.'))
    valorDois = float(input(f'Digite o segundo numero: ').replace(',', '.'))

    print('O maior numero é', max(valorUm, valorDois))

if __name__ == '__main__':
    main()