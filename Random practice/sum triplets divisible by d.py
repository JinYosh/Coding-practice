def solve(A, d):
    triplets = 0
    for j in range(1, len(A) - 1):
        for i in range(j-1, -1, -1):
            for k in range(j + 1, len(A)):
                sum_ = A[i] + A[j] + A[k]
                if sum_ % d == 0:
                    triplets += 1
    return triplets

if __name__ == "__main__":
    A = [3, 3, 4, 7, 8]
    d = 5
    print("Solve:",solve(A, d))