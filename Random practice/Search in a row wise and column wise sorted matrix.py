def solve(A, x):
    rows = len(A)
    cols = len(A[0])
    i = 0
    j = cols
    while i < rows and j >= 0:
        if A[i][j] == x:
            return (i, j)
        elif A[i][j] > x:
            j -= 1
        else:
            i += 1
    return "Element not found."

if __name__ == "__main__":
    A = []
