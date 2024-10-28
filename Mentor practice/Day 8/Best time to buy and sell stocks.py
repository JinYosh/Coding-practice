def bestTime(A):
    min_ = A[0]
    max_profit = 0
    tempProfit = 0
    for i in range(1, len(A)):
        if min_ < A[i]:
            tempProfit = A[i] - min_
            max_profit = max(tempProfit, max_profit)
        else:
            min_ = A[i]
    return max_profit

if __name__ == "__main__":
    A = [1,4,4,0,4]
    print("Result:",bestTime(A))