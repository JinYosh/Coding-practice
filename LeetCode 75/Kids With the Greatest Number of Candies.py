def solve(A, e_candies):
    max_ = max(A)
    result = []
    for i in range(len(A)):
        t_candies = A[i] + e_candies
        if t_candies >= max_:
            result.append(True)
        else:
            result.append(False)
    return result

if __name__ == "__main__":
    A = [2,3,5,1,3]
    e_candies = 3
    print("Result:",solve(A, e_candies))