import random
import sys

def gerar_cpf():
    cpf = [random.randint(0, 9) for _ in range(9)]

    soma = sum((cpf[i] * (10 - i) for i in range(9)))
    primeiro_digito = (soma * 10 % 11) % 10
    cpf.append(primeiro_digito)

    soma = sum((cpf[i] * (11 - i) for i in range(10)))
    segundo_digito = (soma * 10 % 11) % 10
    cpf.append(segundo_digito)

    return f"{cpf[0]}{cpf[1]}{cpf[2]}.{cpf[3]}{cpf[4]}{cpf[5]}.{cpf[6]}{cpf[7]}{cpf[8]}-{cpf[9]}{cpf[10]}"

def main() -> int:
    f = open('input.txt', 'w')
    
    qtd = 30

    for i in range(0, qtd):
        cpf = gerar_cpf()
        #if i % 2 != 0:
        #    cpf = str(random.randint(0,9)) + cpf[1:len(cpf)-1] + str(random.randint(0,9))
        f.write(cpf + '\n')

    f.close()

if __name__ == '__main__':
    sys.exit(main())