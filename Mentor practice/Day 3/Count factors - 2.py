def factorsCount(num):
    if num <= 0:
        return 0
    i = 1
    count = 0
    while i * i <= num:
        f1 = i 
        if num % f1 == 0:
            f2 = num // f1
            if f1 == f2:
                count += 1
            else:
                count += 2
        i += 1
    return count

if __name__ == "__main__":
    num = 1
    print("Result:",factorsCount(num))