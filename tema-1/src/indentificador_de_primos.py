if __name__ == '__main__':

    print('*************** Indentificador de números primos *********************')

    # declaração do número que será verificado
    numero = int(input('Qual o número? \n'))

    quantidade_divisores = 0

    for divisor in range(1, numero + 1):

        if numero % divisor == 0:
            quantidade_divisores += 1

    if quantidade_divisores == 2:
        print('{} é primo!!'.format(numero))
    else:
        print('{} não é primo!!'.format(numero))