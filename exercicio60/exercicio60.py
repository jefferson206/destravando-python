from listaExercicio.uteis.util import Util
import time

def main():
    Util().enunciado('FAÇA UM PROGRAMA QUE IMPRIME A SOMA DE TODOS OS NÚMEROS ÍMPARES ENTRE DOIS NÚMEROS QUAISQUER, INCLUINDO- OS.')

    primeiroValor = int(input('Digite um valor: '))
    segundoValor = int(input('Digite um outro valor: '))

    if primeiroValor > segundoValor:
        temp = primeiroValor
        primeiroValor = segundoValor
        segundoValor = temp

    soma = 0
    for contador in range(primeiroValor, segundoValor+1):
        if contador % 2:
            soma += contador

    try:
        print('\nA soma dos numeros impares entre {} e {} é de: {}'.format(temp, primeiroValor, soma))
    except:
        print('\nA soma dos numeros impares entre {} e {} é de: {}'.format(primeiroValor, segundoValor, soma))



if __name__ == '__main__':
    main()
