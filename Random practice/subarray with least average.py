def solve(A, k):
    least_avg = (10 ** 9) + 7
    least_avg_index = []
    temp_avg = 0
    sum_ = 0
    for i in range(k):
        sum_ += A[i]
    temp_avg = (sum_ / k)
    i = k
    last = 0
    while (i < len(A)):
        prev_ = A[last]
        last += 1
        sum_ += A[i]
        sum_ -= prev_
        temp_avg = sum_ /k
        if temp_avg < least_avg:
            least_avg = temp_avg
            least_avg_index = [last, i]
        i += 1
    return least_avg_index

if __name__ == "__main__":
    A = [3, 7, 5, 20, -10, 0, 12]#[3, 7, 90, 20, 10, 50, 40]
    k = 2#3
    print("Result:",solve(A, k))

