from listaExercicio.uteis.util import Util

def main():
    Util().enunciado('FAÇA UM PROGRAMA QUE LEIA O VALOR DE UM PRODUTO E IMPRIMA O VALOR COM DESCONTO, TENDO EM VISTA QUE O DESCONTO FOI DE 12 %')

    valor = float(input(f'Digite o valor do produto: ').replace(',', '.'))
    desconto = (valor*12/100)
    print('Seu produto com desconto é de:', round(valor-desconto, 2))

if __name__ == '__main__':
    main()