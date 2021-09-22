from listaExercicio.uteis.util import Util

def main():
    Util().enunciado('LEIA O SALÁRIO DE UM FUNCIONÁRIO. CALCULE E IMPRIMA O VALOR DO NOVO SALÁRIO, SABENDO QUE ELE RECEBEU UM AUMENTO DE 25 %.')

    valor = float(input(f'Digite o seu salário: ').replace(',', '.'))
    reajuste = (valor*0.25)+valor
    print('Seu reajuste salarial é de:', round(reajuste, 2))

if __name__ == '__main__':
    main()