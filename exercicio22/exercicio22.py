from listaExercicio.uteis.util import Util

def main():
    Util().enunciadoEmDuasPartes('LEIA UM NÚMERO FORNECIDO PELO USUÁRIO. SE ESSE NÚMERO FOR POSITIVO, CALCULE A RAIZ QUADRADA DO NÚMERO. ',
                     'SE O NÚMERO FOR NEGATIVO, MOSTRE UMA MENSAGEM DIZENDO QUE O NÚMERO É INVÁLIDO.', 120)

    valor = float(input(f'Digite um numero qualquer: ').replace(',', '.'))

    if (valor >= 0):
        print('A raiz quadrada de {} é: {}'.format(valor, pow(valor, 1/2)))
    else:
        print('Numero invalido, valor deve ser valor positivo')

if __name__ == '__main__':
    main()