import sys
import typing
import re
import numpy as np
from pprint import pprint


def valida_cpf(cpf):
    cpf = ''.join(filter(str.isdigit, cpf))

    if len(cpf) != 11:
        return False

    if cpf == cpf[0] * 11:
        return False

    soma = sum(int(cpf[i]) * (10 - i) for i in range(9))
    primeiro_digito_verificador = (soma * 10 % 11) % 10
    if int(cpf[9]) != primeiro_digito_verificador:
        return False

    soma = sum(int(cpf[i]) * (11 - i) for i in range(10))
    segundo_digito_verificador = (soma * 10 % 11) % 10
    if int(cpf[10]) != segundo_digito_verificador:
        return False

    return True

def main() -> int:
    bias = -1
    W0 = -1
    learning_rate = 0.01
    f = open('input.txt', 'r')
    lines = f.readlines()

    training_steps = 10000

    Wi = [None] * 11
    Wi[0] = 1; Wi[1] = 1; Wi[2] = 1; Wi[3] = 1; Wi[4] = 1
    Wi[5] = 1; Wi[6] = 1; Wi[7] = 1; Wi[8] = 1; Wi[9] = 1; Wi[10] = 1

    for i in range(0,training_steps):
        training = []

        for line in lines:
            if line.strip() != '':
                Di = [None] * 12
                cpf = ''.join(filter(str.isdigit, line))
                Xi = cpf
                saida = 0

                for i in range(0, len(Xi)):
                    saida += int(Xi[i]) * Wi[i]
                saida += W0 + bias
                ativacao = 1 if saida >= 0 else -1
                predicao = 1 if valida_cpf(cpf) else -1
                erro = predicao - ativacao
                Di[0] = erro
                for i in range(0, len(Xi)):
                    Di[i+1] = learning_rate * int(Xi[i]) * erro
                training.append(Di);
        
        training = np.average(training, axis=0)

        for i in range(0, len(Wi)):
            Wi[i] = Wi[i] + training[i+1]
    
    f.close()
    f = open('pesos.txt', 'w')
    for i in range(0, len(Wi)):
        f.write(str(Wi[i])+"\n")
    f.close()

    #training.append(
    #    {
    #        'cpf': Xi,
    #       'saida': saida,
    #        'ativacao': ativacao,
    #        'predicao': predicao,
    #        'atual': 'CORRETO' if ativacao > 0 else 'INCORRETO',
    #        'alvo': 'CORRETO' if predicao > 0 else 'INCORRETO',
    #        'erro': erro,
    #    }
    #)



if __name__ == '__main__':
    sys.exit(main())