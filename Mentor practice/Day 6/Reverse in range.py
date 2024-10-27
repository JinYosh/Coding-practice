def reverseRange(A, b, c):
    while b < c:
        temp = A[b]
        A[b] = A[c]
        A[c] = temp
        b += 1
        c -= 1
    return A
if __name__ == "__main__":
    A = [2, 5, 6]
    b = 0
    c = 2
    print("Result:",reverseRange(A, b, c))