from listaExercicio.uteis.util import Util
import time

def main():
    Util().enunciado('FAÇA UM PROGRAMA QUE PEÇA AO USUÁRIO PARA DIGITAR 10 VALORES E SOME-OS.')

    somaDosValores = 0
    for contador in range(1, 11):
        valor = int(input(f'Digite o {contador}ª valor: '))
        somaDosValores += valor

    print('\nA soma de todos os valores digitados foi de:', somaDosValores)

if __name__ == '__main__':
    main()
