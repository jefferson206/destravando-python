from listaExercicio.uteis.util import Util

def main():
    Util().enunciadoEmDuasPartes('LEIA UMA TEMPERATURA EM GRAUS KELVIN E APRESENTE-A CONVERTIDA EM GRAUS CELSIUS. ',
                                 'A FÓRMULA DE CONVERSÃO É : C = K − 273 . 15 , SENDO C A  TEMPERATURA EM  CELSIUS  E K A  TEMPERATURA EM KELVIN.', 180)
    kelvin = round(float(input(f'Digite a temperatura em Kelvin: ').replace(',', '.')), 2)
    celsius = round(kelvin-237.15, 2)
    print('\nTemperatura digitada: ', kelvin)
    print('Temperatura em Celsius: ', celsius)

if __name__ == '__main__':
    main()

