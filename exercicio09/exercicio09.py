from listaExercicio.uteis.util import Util

def main():
    Util().enunciadoEmDuasPartes('LEIA UM VALOR DE COMPRIMENTO EM POLEGADAS E APRESENTE-O CONVERTIDO EM CENTÍMETROS.',
                                 ' A FÓRMULA DE CONVERSÃO É : C = P ∗ 2 , 54 , SENDO C O COMPRIMENTO EM  CENTÍMETROS E P O COMPRIMENTO EM POLEGADAS.', 180)

    polegadas = round(float(input(f'Digite o comprimento em polegadas: ').replace(',', '.')), 2)
    centimentros = round(polegadas*2.54, 2)

    print('\nComprimento em polegadas: ', polegadas)
    print('Comprimento eem centimetros: ', centimentros)

if __name__ == '__main__':
    main()

