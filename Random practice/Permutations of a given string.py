def solve(A):
    ans_list = []
    permutation(ans_list, A, 0)
    return ans_list

def permutation(ans_list ,A, l):
    if l == len(A) - 1:
        ans_list.append(A)
    for i in range(l, len(A), 1):
        A = swap(A, l, i)
        permutation(ans_list, A, l + 1)
        A = swap(A, i, l)

def swap(A, l, i):
    new_str = ""
    for k in range(len(A)):
        if k == l:
            new_str += A[i]
        elif k == i:
            new_str += A[l]
        else:
            new_str += A[k]
    return new_str

if __name__ == "__main__":
    A = "ABC"
    print("Result:",solve(A))