def solve(A, n):
    ans_list = []
    for num in A:
        temp = (num + n) if num % 2 != 0 else (num - n)
        ans_list.append(temp)
    return ans_list

if __name__ == "__main__":
    A = [3, 4, 9]
    n = 3
    print("Result:",solve(A, n))