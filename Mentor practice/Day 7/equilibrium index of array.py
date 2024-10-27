def equilibIndexBF(A):
    ans_list = []
    for j in range(len(A)):
        l_sum = 0
        r_sum = 0
        for i in range(j-1, -1, -1):
            l_sum += A[i]
        for k in range(j+1, len(A)):
            r_sum += A[k]
        if l_sum == r_sum:
            ans_list.append(j)
    return min(ans_list) if len(ans_list) > 0 else -1

def equilibIndexPS(A):
    PS = [A[0]]
    ans_ = (10 ** 9) + 7
    for i in range(1, len(A)):
        PS.append(PS[i-1] + A[i])
    for i in range(len(A)-1, -1, -1):
        l_sum = PS[i - 1] if i-1 > -1 else 0
        r_sum = PS[len(A)-1] - PS[i]
        if l_sum == r_sum:
            ans_ = i
    return -1 if (ans_ == (10 ** 9) + 7) else ans_

if __name__ == "__main__":
    A = [-7,1,5,2,-4,3,0]
    print("Result:",equilibIndexPS(A))
