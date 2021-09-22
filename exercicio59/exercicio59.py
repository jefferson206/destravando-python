from listaExercicio.uteis.util import Util
import time

def main():
    Util().enunciado('LEIA UM NÚMERO INTEIRO, E CONTE O NÚMERO TOTAL DE DÍGITOS. EX: 3 (1 DÍGITO), 10 (2 DÍGITOS), 233 (3 DÍGITOS), ETC.')

    valor = int(input('Digite um valor: '))

    tamanho = len(str(valor))

    if tamanho == 1:
        texto = 'Digito'
    else:
        texto = 'Digitos'
    print(tamanho, texto)


if __name__ == '__main__':
    main()
