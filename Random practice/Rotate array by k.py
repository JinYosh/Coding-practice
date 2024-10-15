#def solve(A, k):
#    k = k % len(A)
#    new_arr = [0 for _ in range(len(A))]
#
#    #
#    start_ = k
#    i = 0
#    while start_ < len(A):
#        new_arr[i] = A[start_]
#        i += 1
#        start_ += 1
#    #
#    start_ = 0
#    while i < len(new_arr):
#        new_arr[i] = A[start_]
#        i += 1
#        start_ += 1
#    return new_arr

# In place
def solve(A, k):
    k = k % len(A)
    A = reverse(A, 0, k - 1)
    A = reverse(A, k, len(A) - 1)
    A = reverse(A, 0, len(A) - 1)
    return A

def reverse(A, start, end):
    while(start <= end):
        temp = A[start]
        A[start] = A[end]
        A[end] = temp

        start += 1
        end -= 1
    return A

if __name__ == "__main__":
    A = [1, 2, 3, 4, 5, 6]
    k = 0
    print("Result:",solve(A, k))
