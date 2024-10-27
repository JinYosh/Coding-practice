def powerFunc(a, b):
    ans_ = 1
    while b > 0:
        ans_ *= a
        b -= 1
    return ans_

if __name__ == "__main__":
    a = 1
    b = 10
    print("Result:",powerFunc(a, b))