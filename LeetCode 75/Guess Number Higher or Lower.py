def guessNumber(n):
    L = 0
    R = n
    while L <= R:
        mid = (L + R) // 2
        g = guess(mid)
        if g == -1:
            R = mid - 1
        elif g == 1:
            L = mid + 1
        elif g == 0:
            return mid
    return -1


        