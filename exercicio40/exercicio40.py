from listaExercicio.uteis.util import Util


def main():
    Util().enunciadoEmDuasPartes(
        'LEIA A DISTANCIA EM KM E A QUANTIDADE DE LITROS DE GASOLINA CONSUMIDOS POR UM CARRO EM UM PERCURSO, ',
        'CALCULE O CONSUMO EM KM/L E ESCREVA UMA MENSAGEM DE ACORDO COM A TABELA ABAIXO:', 140)

    distancia = float(input(f'Digite a distancia percorrida: ').replace(',', '.'))
    litrosConsumidos = float(input(f'Digite quantos litros foram gastos: ').replace(',', '.'))

    media = round(distancia / litrosConsumidos, 2)

    if media < 8:
        print('Venda o carro!', media)
    elif media >= 8 and media <= 12:
        print('Economico...', media)
    else:
        print('Super ECONOMICO!!!', media)


if __name__ == '__main__':
    main()
