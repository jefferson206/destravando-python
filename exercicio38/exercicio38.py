from listaExercicio.uteis.util import Util


def main():
    Util().enunciado('FAÇA UM PROGRAMA QUE LEIA UM NÚMERO E DIGA SE ELE É DIVISÍVEL POR 2 E POR 3. USE ESTRUTURA DE DESVIO CONDICIONAL SIMPLES.')

    valor = int(input('Digite um valor inteiro: '))

    if valor % 2 == 0 and valor % 3 == 0:
        print('O valor {} é divisivel por 2 e por 3'.format(valor))
    else:
        print('Este numero não é divisivel por 2 e 3 ao mesmo tempo')


if __name__ == '__main__':
    main()
