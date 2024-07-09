import sys
import typing
import re

def main() -> int:
    bias = -1
    # Entradas (11)
    Xi = '50108980049'
    # Pesos (Um peso para cada numero do CPF). Obtido no treinamento
    Wi = [None] * 11
    W0 = -1
    
    f = open('pesos.txt', 'r')
    lines = f.readlines()
    for i in range(0, 11):
        Wi[i] = float(lines[i])
    f.close()

    saida = 0
    for i in range(0, len(Xi)):
        saida += int(Xi[i]) * Wi[i]
    saida += W0 + bias
    print(saida)

    print('CPF Valido' if saida >= 0 else 'CPF Invalido')

if __name__ == '__main__':
    sys.exit(main())