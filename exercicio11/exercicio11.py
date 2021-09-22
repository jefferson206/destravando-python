from listaExercicio.uteis.util import Util

def main():
    Util().enunciado('PEÇA AO USUÁRIO QUATRO NOTAS, CALCULE A MEDIA ARITMÉTICA E IMPRIMA O RESULTADO.')

    somaDasNotas = 0.0
    for nota in range(1, 5):
        valor = float(input(f'Digite a {nota}ª nota: ').replace(',', '.'))
        somaDasNotas += valor

    print('\nA media é de: ', somaDasNotas/4)

if __name__ == '__main__':
    main()