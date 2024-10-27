def inPlacePS(A):
    for i in range(1, len(A)):
        A[i] = A[i-1] + A[i]

if __name__ == "__main__":
    A = [1,2,3,4,5]
    inPlacePS(A)
    print("Result:",A)