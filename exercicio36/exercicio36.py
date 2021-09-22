from listaExercicio.uteis.util import Util


def main():
    Util().enunciado('FAÇA UM ALGORITMO QUE LEIA UMA VARIÁVEL E DIVIDA POR 10 SE ESTIVER NO INTERVALO ENTRE 0 E 100 CASO ESTEJA FORA, DIVIDA POR 2. IMPRIMA O RESULTADO')

    valor = int(input('Digite o um valor: '))

    if valor < 0:
        print('valor não pode ser negativo...')
        return
    if valor > 100:
        print('Resultado: ', round(valor/2, 2))
    else:
        print('Resultado: ', round(valor/10, 2))


if __name__ == '__main__':
    main()
