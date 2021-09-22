from listaExercicio.uteis.util import Util

def main():
    Util().enunciado('PEÇA AO USUÁRIO PARA DIGITAR UM NÚMERO REAL E IMPRIMA A QUINTA PARTE DESTE NÚMERO.')

    valor = float(input(f'Digite um numero real: ').replace(',', '.'))

    print('\nA quinta parte de {} é de: {} '.format(valor, (valor*(1/5))))

if __name__ == '__main__':
    main()