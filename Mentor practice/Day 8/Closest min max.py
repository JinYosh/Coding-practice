def closeMinMax(A):
    min_ = (10 ** 9) + 7
    max_ = - ((10 ** 9) + 7)
    for num in A:
        min_ = min(min_, num)
        max_ = max(max_, num)
    min_i = -1
    max_i = -1
    min_len = len(A)
    for i in range(len(A)):
        if A[i] == min_ or A[i] == max_:
            if A[i] == min_:
                min_i = i
            if A[i] == max_:
                max_i = i
            if min_i != -1 and max_i != -1:
                temp_len = abs(min_i - max_i) + 1
                min_len = min(temp_len, min_len)
    return min_len


if __name__ == "__main__":
    A = [1,0,0,5,0,9,5,9]
    print("Result:",closeMinMax(A))

