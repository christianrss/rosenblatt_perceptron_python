import sys
import typing
import re

def main() -> int:
    bias = -1
    
    cpf_fake = '911.092.510-41'
    # Entradas (11)
    Xi = re.split('[. -]', cpf_fake)
    # Pesos (Um peso para cada numero do CPF). Obtido no treinamento
    Wi = [None] * 11
    Wi[0] = -1; Wi[1] = 0; Wi[2] = 0; Wi[3] = 0; Wi[4] = 0; Wi[5] = 0
    Wi[6] = 0; Wi[7] = 0; Wi[8] = 0; Wi[9] = 0; Wi[10] = 0

    print(Wi)

if __name__ == '__main__':
    sys.exit(main())