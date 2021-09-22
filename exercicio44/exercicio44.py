from listaExercicio.uteis.util import Util


def main():
    Util().enunciado('FAÇA UM PROGRAMA QUE IMPRIME A SOMA DE TODOS OS NÚMEROS PARES ENTRE DOIS NÚMEROS QUAISQUER, INCLUINDO- OS.')

    primeiroValor = int(input('Digite o primeiro valor: '))
    segundoValor = int(input('Digite o segundo valor: '))
    quantidade = 0

    if primeiroValor > segundoValor:
        temp = primeiroValor
        primeiroValor = segundoValor
        segundoValor = temp

    for valores in range(primeiroValor, segundoValor+1):
        if valores % 2 == 0:
            quantidade += valores

    try:
        print('A soma dos numeros pares entre {} e {} é de: {}'.format(temp, primeiroValor, quantidade))
    except:
        print('A soma dos numeros pares entre {} e {} é de: {}'.format(primeiroValor, segundoValor, quantidade))


if __name__ == '__main__':
    main()
