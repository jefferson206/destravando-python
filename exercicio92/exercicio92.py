from listaExercicio.uteis.util import Util
from math import pi


def main():
    Util().enunciadoEmDuasPartes('FAÇA UMA FUNÇÃO QUE RECEBA A ALTURA E O RAIO DE UM CILINDRO CIRCULAR E RETORNE O VOLUME DO CILINDRO.',
                     'O VOLUME DE UM CILINDRO CIRCULAR E CALCULADO POR MEIO DA SEGUINTE FÓRMULA: V = Π ∗ RAIO 2 ∗ ALTURA.')

    altura = float(input('Digite a altura do cilindro: ').replace(',', '.'))
    raio = float(input('Digite o raio do cilindro: ').replace(',', '.'))

    print('\nVolume do cilindro é de:', checarVolumeDoCilindro(altura, raio))


def checarVolumeDoCilindro(altura, raio):
    volume = pi * raio*2 * altura
    return round(volume, 2)


if __name__ == '__main__':
    main()
