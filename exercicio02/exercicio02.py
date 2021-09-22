from listaExercicio.uteis.util import Util

def main():
    Util().enunciado('FAÇA UM PROGRAMA QUE LEIA UM NÚMERO REAL E O IMPRIMA.')
    valor = float(input('Digite um valor quebrado: ').replace(',', '.'))
    print('Valor digitado: ', valor)

if __name__ == '__main__':
    main()