from listaExercicio.uteis.util import Util


def main():
    Util().enunciadoEmDuasPartes('CRIE UMA FUNÇÃO QUE ACEITE O NOME DO FUNCIONÁRIO E SEU SALÁRIO E EXIBA AMBOS.',
                                 'SE O SALÁRIO ESTIVER FALTANDO NA CHAMADA DE FUNÇÃO, ATRIBUA O VALOR PADRÃO 1000 AO SALÁRIO.')

    funcionario = str(input('Digite o nome do funcionário: '))
    try:
        salario = int(input('Digite o valor do salário: '))
    except:
        salario = 1000

    chamaFuncionario(funcionario, salario)


def chamaFuncionario(funcionario, salario):
    print('\nFuncionário: {} \nSalário: {}'.format(funcionario, salario))

if __name__ == '__main__':
    main()
