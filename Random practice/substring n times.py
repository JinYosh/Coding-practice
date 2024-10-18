def solve(A):
    temp_str = ""
    for i in range(len(A)):
        temp_str += A[i]
        if A[i:].find(temp_str) == 1:
            return True
    return False

if __name__ == "__main__":
    A = "abcdabc"
    print("Result:",solve(A))