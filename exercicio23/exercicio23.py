from listaExercicio.uteis.util import Util


def main():
    Util().enunciadoEmDuasPartes('LEIA UM NÚMERO REAL. SE O NÚMERO FOR POSITIVO IMPRIMA A RAIZ QUADRADA.',
                                 'DO CONTRÁRIO, IMPRIMA O NÚMERO AO QUADRADO.', 80)

    valor = float(input(f'Digite um numero qualquer: ').replace(',', '.'))

    if valor >= 0:
        print('A raiz quadrada de {} é: {}'.format(valor, pow(valor, 1 / 2)))
    else:
        print('O quadrado de {} é: {}'.format(valor, pow(valor, 2)))


if __name__ == '__main__':
    main()
