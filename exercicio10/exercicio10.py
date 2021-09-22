from listaExercicio.uteis.util import Util

def main():
    Util().enunciado('FAÇA A LEITURA DE TRÊS VALORES E APRESENTE COMO RESULTADO A SOMA DOS QUADRADOS DOS TRÊS VALORES LIDOS.')

    soma = 0.0
    for indice in range(0, 3):
        valor = float(input(f'Digite o {indice+1}º valor inteiro: ').replace(',', '.'))**2
        soma += valor

    print('\nA soma dos valores é ao quadrado é de: ', soma)

if __name__ == '__main__':
    main()