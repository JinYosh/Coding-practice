def isPrime(num):
    if num == 1:
        return False
    totalFactors = countFactors(num)
    if totalFactors == 2:
        return True
    return False

def countFactors(num):
    i = 1
    count = 0
    while i * i <= num:
        f1 = i
        if num % i == 0:
            f2 = num // f1
            if f1 == f2:
                count += 1
            else:
                count += 2
        i += 1
    return count

def isPrimeBLoop(num):
    if num == 1:
        return False
    f1 = 1
    count = 0
    while f1 * f1 <= num:
        if num % f1 == 0:
            f2 = num // f1
            if f1 == f2:
                count += 1
            else:
                count += 2
        if count > 2:
            return False
        f1 += 1
    return True


if __name__ == "__main__":
    num = 0
    print("Result:",isPrimeBLoop(num))
