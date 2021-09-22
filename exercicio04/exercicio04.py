from listaExercicio.uteis.util import Util

def main():
    Util().enunciado('PEÇA AO USUÁRIO PARA DIGITAR UM NÚMERO REAL E IMPRIMA O RESULTADO DO QUADRADO DESSE NÚMERO..')

    valor = round(float(input(f'Digite um numero quebrado: ').replace(',', '.'))**2, 2)

    print('\nO quadrado do valor digitado é de: ', valor)

if __name__ == '__main__':
    main()