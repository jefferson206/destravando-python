from listaExercicio.uteis.util import Util
import time

def main():
    Util().enunciado('FAÇA UM PROGRAMA QUE LEIA 10 INTEIROS E IMPRIMA SUA MÉDIA.')

    somaDosValores = 0.0
    for contador in range(1, 11):
        valor = float(input(f'Digite o {contador}ª valor: ').replace(',', '.'))
        somaDosValores += valor

    media = float(somaDosValores/10)

    print('\nA média de todos os valores digitados foi de:', media)

if __name__ == '__main__':
    main()
