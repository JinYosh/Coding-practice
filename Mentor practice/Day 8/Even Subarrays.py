def solve(A):
    if len(A) % 2 != 0:
        return "No"
    if A[0] % 2 != 0 or A[-1] % 2 != 0:
        return "No"
    return "Yes"

if __name__ == "__main__":
    A = [2,1,3,4]
    print("Result:",solve(A))