from listaExercicio.uteis.util import Util


def main():
    Util().enunciadoEmDuasPartes('ELABORE UM ALGORITMO QUE DADA A IDADE DE UM NADADOR CLASSIFICA-O EM UMA DAS SEGUINTES CATEGORIAS: ',
                                 'INFANTIL A = 5-7 ANOS, INFANTIL B = 8-10 ANOS, JUVENIL A  = 11-13 ANOS, JUVENIL B = 14-17 ANOS, ADULTO = MAIORES DE 18 ANOS.', 160)

    idade = int(input(f'Digite sua idade: '))

    if idade <= 7:
        print('INFANTIL A')
    if idade >=8 and idade <= 10:
        print('INFANTIL B')
    if idade >= 11 and idade <= 13:
        print('JUVENIL A')
    if idade >=14 and idade <= 17:
        print('JUVENIL B')
    if idade >= 18:
        print('ADULTO')


if __name__ == '__main__':
    main()
