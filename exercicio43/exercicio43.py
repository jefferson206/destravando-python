from listaExercicio.uteis.util import Util


def main():
    Util().enunciado('FAÇA UM PROGRAMA PARA CONTAR A QUANTIDADE DE NÚMEROS PARES ENTRE DOIS NÚMEROS QUAISQUER')

    primeiroValor = int(input('Digite o primeiro valor: '))
    segundoValor = int(input('Digite o segundo valor: '))
    quantidade = 0

    if primeiroValor > segundoValor:
        temp = primeiroValor
        primeiroValor = segundoValor
        segundoValor = temp

    for valores in range(primeiroValor, segundoValor+1):
        if valores % 2 == 0:
            quantidade += 1

    try:
        print('Existem {} numeros pares de {} a {}'.format(quantidade, temp, primeiroValor))
    except:
        print('Existem {} numeros pares de {} a {}'.format(quantidade, primeiroValor, segundoValor))


if __name__ == '__main__':
    main()
