def occurenecs(a, b):
    occurs = 0
    for num in a:
        if num == b:
            occurs += 1
    return occurs

if __name__ == "__main__":
    a = [1, 2, 1]
    b = 3
    print("Result:",occurenecs(a, b))