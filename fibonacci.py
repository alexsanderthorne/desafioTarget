n = 34
vetorFibonacci = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]


def fibonacci():
    for i in range(len(vetorFibonacci)):
        if(n == vetorFibonacci[i]):
            nAnterior = vetorFibonacci[i-1]
            nAnteAnterior = vetorFibonacci[i-2]
            if(n == nAnterior + nAnteAnterior):
                return True


print(fibonacci())
