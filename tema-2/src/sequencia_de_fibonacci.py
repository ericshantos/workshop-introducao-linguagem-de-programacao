if __name__ == '__main__':

    print('****************** Sequência de Fibonacci (até o 10° elemento) *********************')

    ultimo = 1
    penultimo = 0

    for sequencia in range(1,11):

        fibonacci = ultimo + penultimo
        penultimo = ultimo
        ultimo = fibonacci

        print('{}° elemento: {}'.format(sequencia,fibonacci))