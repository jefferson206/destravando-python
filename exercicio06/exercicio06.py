from listaExercicio.uteis.util import Util

def main():
    Util().enunciadoEmDuasPartes('LEIA UMA TEMPERATURA EM GRAUS CELSIUS E APRESENTE-A CONVERTIDA EM GRAUS FAHRENHEIT. ',
                     'A FÓRMULA DE CONVERSÃO É : F = C∗( 9 . 0 / 5 . 0 )+ 32 . 0 , SENDO F A TEMPERATURA  EM FAHRENHEIT E C A TEMPERATURA EM CELSIUS.', 180)
    celsius = round(float(input(f'Digite a temperatura em Celsius: ').replace(',', '.')), 2)
    fahrenheit = celsius*(9.0/5.0)+32
    print('\nTemperatura digitada: ', celsius)
    print('Temperatura em Fahrenheit: ', fahrenheit)

if __name__ == '__main__':
    main()