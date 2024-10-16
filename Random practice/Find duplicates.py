def solve(A):
    dup_list = []
    set_ = set()
    for i in range(len(A)):
        if A[i] in set_:
            dup_list.append(A[i])
        else:
            set_.add(A[i])
    return dup_list

if __name__ == "__main__":
    A = [1, 2, 3, 6, 3, 6, 1]
    print("Result:",solve(A))