import sys
import typing
import re

def main() -> int:
    bias = -1
    # Entradas (11)
    Xi = '91109251041'
    # Pesos (Um peso para cada numero do CPF). Obtido no treinamento
    Wi = [None] * 11
    W0 = -1
    Wi[0] = 0; Wi[1] = 0; Wi[2] = 0; Wi[3] = 0; Wi[4] = 0
    Wi[5] = 0; Wi[6] = 0; Wi[7] = 0; Wi[8] = 0; Wi[9] = 0; Wi[10] = 0;

    saida = 0
    for i in range(0, len(Xi)):
        saida += int(Xi[i]) * Wi[i]
    saida += W0 + bias

    print(saida)

if __name__ == '__main__':
    sys.exit(main())