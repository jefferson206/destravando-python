from listaExercicio.uteis.util import Util


def main():
    Util().enunciado('FAÇA UMA FUNÇÃO QUE RECEBA DOIS NÚMEROS INTEIROS POSITIVOS POR PARÂMETRO E RETORNE A SOMA DOS N NUMEROS INTEIROS EXISTENTES ENTRE ELES.')

    primeiro = int(input('Digite um valor: '))
    segundo = int(input('Digite um outro valor: '))
    maior = max(primeiro, segundo)
    menor = min(primeiro, segundo)

    print('\nSoma dos valores entre eles é de:', somar(maior, menor))



def somar(primeiro, segundo):
    if primeiro == segundo:
        return 0
    else:
        return primeiro + somar(primeiro - 1, segundo)

if __name__ == '__main__':
    main()
