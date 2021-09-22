from listaExercicio.uteis.util import Util
import time

def main():
    Util().enunciadoEmDuasPartes('FAÇA UM ALGORITMO UTILIZANDO O COMANDO WHILE QUE MOSTRA UMA CONTAGEM REGRESSIVA NA TELA, INICIANDO EM 10 E TERMINANDO EM 0.',
                                 'MOSTRAR UMA MENSAGEM "FIM!” APÓS A CONTAGEM', 140)

    contador = 10
    print('Contagem regressiva... ')
    while contador >= 0:
        print(contador)
        time.sleep(0.3)
        contador -= 1

    print(' --- FIM ---')

if __name__ == '__main__':
    main()
