from listaExercicio.uteis.util import Util

def main():
    Util().enunciadoEmDuasPartes('LEIA UM ÂNGULO EM GRAUS E APRESENTE-O CONVERTIDO EM RADIANOS. ',
                                 'A FÓRMULA DE CONVERSÃO É R = G ∗ PI/ 180 , SENDO G O ANGULO EM GRAUS E R EM  RADIANOS E PI = 3.14 .', 180)

    PI = 3.14
    graus = round(float(input(f'Digite o angulo em graus: ').replace(',', '.')), 2)
    radiano = round(graus*PI/180, 4)

    print('\nAngulo digitada: ', graus)
    print('Angulo em radianos: ', radiano)

if __name__ == '__main__':
    main()

