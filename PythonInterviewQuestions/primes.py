def getPrimeNums(n):
    primes = []
    tf = [True] * (n+1)
    for i in range(2, len(tf)):
        if tf[i]:
            primes.append(i)
            for j in range(i+i, len(tf), i):
                tf[j] = False
    return primes


def main():
    print(getPrimeNums(100))


if __name__ == '__main__':
    main()
