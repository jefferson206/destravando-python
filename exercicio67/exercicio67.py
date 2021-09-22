from listaExercicio.uteis.util import Util

def main():
    Util().enunciado('ESCREVA UM PROGRAMA QUE RECEBA DUAS LISTAS E RETORNE TRUE SE ELAS TIVEREM PELO MENOS UM ELEMENTO EM COMUM.')

    primeiraLista = [1, 2, 2, 3, 5, 7, 10, 8, 5]
    segundaLista = [10, 11, 12, 13, 14, 16]

    valorComum = set(primeiraLista) & set(segundaLista)
    if valorComum:
        print('Elementos iguais:', list(valorComum))
    else:
        print('Não há valores comuns entre a lista')


if __name__ == '__main__':
    main()
