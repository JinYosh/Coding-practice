def perfectNum(num):
    i = 1
    sum_ = 0
    while i * i <= num:
        f1 = i
        if num % f1 == 0:
            f2 = num // f1 
            if f1 == f2 or f1 == 1:
                sum_ += f1
            else:
                sum_ += (f1 + f2)
        i += 1
    return 1 if sum_ == num else 0

if __name__ == "__main__":
    a = 6
    print("Result:",perfectNum(a))
