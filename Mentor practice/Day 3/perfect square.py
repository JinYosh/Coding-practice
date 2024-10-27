def isPerfectSquare(num):
    i = 1
    while True:
        if i * i == num:
            return 1
        elif i * i > num:
            return 0
        i += 1
    

if __name__ == "__main__":
    num = 6
    print("Result:",isPerfectSquare(num))