def solve(t):
    n = 0
    temp_t = 1
    prev_t = 0
    while(temp_t <= t):
        prev_t = temp_t
        temp_t += (2**n) * 3
        n += 1
    diff_t = t - prev_t
    print("n: {} | prev_t: {} | diff_t: {}".format(n, prev_t, diff_t))
    value = ((2 ** (n - 1)) * 3) - diff_t
    return value

if __name__ == "__main__":
    t = 16
    print("Result:",solve(t))