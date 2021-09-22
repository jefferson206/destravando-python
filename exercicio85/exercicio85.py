from listaExercicio.uteis.util import Util


def main():
    Util().enunciado('ESCREVA UMA FUNÇÃO RECURSIVA PARA CALCULAR A SOMA DOS NÚMEROS DE 0 A 10')

    soma = int(input('somando de 0 até: '))
    print('Soma: ', somar(soma))

def somar(valor):
    if valor == 0:
        return 0
    else:
        return valor + somar(valor - 1)

if __name__ == '__main__':
    main()
