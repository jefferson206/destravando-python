from listaExercicio.uteis.util import Util

def main():
    Util().enunciado('ESCREVA UM PROGRAMA QUE LEIA AS COORDENADAS X E Y DE PONTOS NO R 2 E CALCULE SUA DISTÂNCIA DA ORIGEM ( 0 , 0 ) .')

    coordenadaXa = int(input(f'Digite a coordenada do primeiro ponto x: '))
    coordenadaXb = int(input(f'Digite a coordenada do segundo ponto x: '))
    coordenadaYa = int(input(f'Digite a coordenada do primeiro ponto y: '))
    coordenadaYb = int(input(f'Digite a coordenada do segundo ponto y: '))
    distancia = ((coordenadaXa-coordenadaYa)**2 + (coordenadaXb-coordenadaYb)**2)**0.5

    print('A distancia entre os pontos é de:', round(distancia, 2))

if __name__ == '__main__':
    main()