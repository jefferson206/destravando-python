from listaExercicio.uteis.util import Util


def main():
    Util().enunciado('FAÇA UM PROGRAMA QUE IMPRIME A QUANTIDADE DE NÚMEROS PARES DE 100 ATÉ 200 INCLUINDO- OS.')

    cem = 100
    duzentos = 201
    quantidade = 0

    for valores in range(cem, duzentos):
        if valores % 2 == 0:
            quantidade += 1

    print('Existem {} numeros pares de 100 a 200'.format(quantidade))


if __name__ == '__main__':
    main()
