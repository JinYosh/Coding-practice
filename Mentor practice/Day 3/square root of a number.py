def squareRoot(num):
    if num == 1:
        return num
    i = 1
    while True:
        if i * i == num:
            return i
        elif i * i > num:
            break
        i += 1
    return -1

def squareRBin(num):
    if num == 1:
        return num
    l = 0
    r = num
    prev_ans = None
    while l <= r:
        mid = (l + r) // 2
        if mid * mid == num:
            return mid
        elif mid * mid > num:
            r = mid - 1
        else:
            prev_ans = mid
            l = mid + 1
    return prev_ans


if __name__ == "__main__":
    num = 0
    print("Result:",squareRBin(num))