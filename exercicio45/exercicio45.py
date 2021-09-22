from listaExercicio.uteis.util import Util


def main():
    Util().enunciado('FAÇA UM PROGRAMA QUE CALCULE O FATORIAL DE UM NÚMERO.')

    valor = int(input('Digite o valor: '))
    fatorial = 1
    combinacao = 2

    while combinacao <= valor:
        fatorial *= combinacao
        combinacao += 1

    print('O fatorial de {} é de: {}'.format(valor, fatorial))

if __name__ == '__main__':
    main()
