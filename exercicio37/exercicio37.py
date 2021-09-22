from listaExercicio.uteis.util import Util


def main():
    Util().enunciadoEmDuasPartes('CRIE UM ALGORITMO QUE, DADO O NÍVEL DE ALERTA DE RISCO, IMPRIMA SE ELE FOR GRAVE. ',
                                 'O NÍVEL DE ALERTA É UM NÚMERO QUE VARIA DE 0 A 10. O NÍVEL É CONSIDERADO GRAVE QUANDO ELE É SUPERIOR A 9 .', 120)

    valor = int(input('Digite um valor entre 0 a 10: '))

    if valor < 0 or valor > 10:
        print('valor invalido...')
        return
    if valor >= 9:
        print('GRAVE')
    elif valor >=5 and valor <8:
        print('MODERADO')
    else:
        print('LEVE')


if __name__ == '__main__':
    main()
