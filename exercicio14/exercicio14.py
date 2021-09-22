from listaExercicio.uteis.util import Util

def main():
    Util().enunciado('LEIA O TAMANHO DO LADO DE UM QUADRADO E IMPRIMA COMO RESULTADO A SUA ÁREA.')

    lado = float(input(f'Digite o lado de um quadrado: ').replace(',', '.'))

    print('A área do quadrado é de:', round(lado*lado, 2))

if __name__ == '__main__':
    main()