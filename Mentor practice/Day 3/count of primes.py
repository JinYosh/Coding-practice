def countPrime(n):
    isPrime = False
    count = 0
    for num in range(2, n + 1):
        isPrime = primeOrNot(num)
        if isPrime:
            count += 1
    return count

def primeOrNot(num):
    i = 1
    cF = 0
    while i * i <= num:
        f1 = i
        if num % f1 == 0:
            f2 = num // f1
            if f1 == f2:
                cF += 1
            else:
                cF += 2
        if cF > 2:
            return False
        i += 1
    print("num: {} | cF: {}".format(num, cF))
    return True

if __name__ == "__main__":
    num = 19
    print("Result:",countPrime(num))