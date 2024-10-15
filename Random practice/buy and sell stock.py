#def solve(A):
#    min_ = A[0]
#    max_profit = 0
#    max_profit_list = []
#    num_changed = False
#    for i in range(1, len(A)):
#        profit = A[i] - min_
#        max_profit = max(max_profit, profit)
#        num_changed = False
#        if min_ > A[i]:
#            min_ = A[i]
#            max_profit_list.append(max_profit)
#            num_changed = True
#    if not num_changed:
#        max_profit_list.append(max_profit)
#    return sum(max_profit_list)

def solve(A):
    min_ = A[0]
    max_profit = 0
    result = 0
    for i in range(1, len(A)):
        if max_profit < (A[i] - min_):
            result += (A[i] - min_)
            max_profit = A[i] - min_
        if min_ > A[i]:
            min_ = A[i]
    return result



#def solve(A):
#    res = 0
#    for i in range(len(A)):
#        if A[i] > A[i - 1]:
#            res += (A[i] - A[i-1])
#    return res

if __name__ == "__main__":
    A = [100, 180, 260, 310, 40, 535, 695] #[4, 2, 2, 2, 4] #
    print("Result:",solve(A))


