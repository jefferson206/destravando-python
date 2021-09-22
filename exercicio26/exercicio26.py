from listaExercicio.uteis.util import Util


def main():
    Util().enunciadoEmDuasPartes('LEIA O SALÁRIO DE UM TRABALHADOR E O VALOR DA PRESTAÇÃO DE UM EMPRÉSTIMO. ',
                                 'SE A PRESTAÇÃO FOR MAIOR QUE 20 % DO SALÁRIO IMPRIMA: EMPRÉSTIMO NÃO CONCEDIDO, CASO CONTRÁRIO IMPRIMA: EMPRÉSTIMO CONCEDIDO.', 140)

    salario = float(input(f'Digite seu salário: ').replace(',', '.'))
    prestacao = float(input(f'Digite o valor da prestação: ').replace(',', '.'))

    emprestimo = (salario*20/100)
    if emprestimo < prestacao:
        print('EMPRÉSTIMO NÃO CONCEDIDO')
    else:
        print('EMPRÉSTIMO CONCEDIDO')

if __name__ == '__main__':
    main()
