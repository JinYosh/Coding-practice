def pickfrombothsides(A, B):
    sum_ = sum(A[:B])
    max_sum = sum_
    i = len(A) - 1
    while B > 0:
        sum_ -= A[B-1] 
        sum_ += A[i]
        max_sum = max(max_sum, sum_)
        B -= 1
        i -= 1
    return max_sum

if __name__ == "__main__":
    A = [5,-2,3,1,2]
    B = 3
    print("Result:",pickfrombothsides(A, B))
