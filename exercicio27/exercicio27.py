from listaExercicio.uteis.util import Util


def main():
    Util().enunciadoEmDuasPartes('LEIA O SALÁRIO DE UM TRABALHADOR E O PERCENTUAL DE IMPOSTO PAGO EM FOLHA.',
                                 'SE O VALOR FOR MAIOR QUE R$ 200 IMPRIMA: ACIMA DE R$ 200,00 , CASO CONTRARIO IMPRIMA: ABAIXO DE R$ 200,00.', 120)

    salario = float(input(f'Digite seu salário: ').replace(',', '.'))
    imposto = float(input(f'Digite a porcentagem de desconto da folha: ').replace(',', '.'))

    valorDesconto = (salario*imposto/100)
    if valorDesconto > 200:
        print('ACIMA DE R$ 200,00')
    else:
        print('ABAIXO DE R$ 200,00')

if __name__ == '__main__':
    main()
