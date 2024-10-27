def makeIt(a, b):
    totalSlices = (a * 3) + b
    return totalSlices // 2

if __name__ == "__main__":
    a = 7
    b = 1
    print("Result:",makeIt(a, b))