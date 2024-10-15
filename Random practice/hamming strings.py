#def solve(A, k):
#    s_1 = ""
#    s_2 = ""
#    s_1_index = 0
#    s_2_index = 0
#    hammer_sum = 0
#    s_1 = A[s_1_index : s_1_index + k]
#    while s_2_index + k < len(A):
#        #s_2 = A[s_2_index : s_2_index + k]
#        s_2 = s_1[1:] + A[k + s_2_index]
#        hammer_sum += findHammerSum(s_1, s_2)
#        s_1 = s_2
#        #s_1_index += 1
#        s_2_index += 1
#
#    return hammer_sum
#        
#def findHammerSum(s1, s2):
#    sum_ = 0
#    index = 0
#    while index < len(s2):
#        if s1[index] != s2[index]:
#            sum_ += 1
#        index += 1
#    print(s1, s2, sum_)
#    return sum_

def solve(A, k):
    hamming_sum = 0
    total_hamming_sum = 0

    for i in range(k):
        if A[i] != A[i + 1]:
            hamming_sum += 1
    total_hamming_sum += hamming_sum
    print(hamming_sum)

    for i in range(1, len(A) - k):
        if A[i-1] != A[i]:
            hamming_sum -= 1
        if A[i + k - 1] != A[k+i]:
            hamming_sum += 1
        print(hamming_sum)
        total_hamming_sum += hamming_sum
    return total_hamming_sum

if __name__ == "__main__":
    A = "aabbcc" #"abccc"
    k = 2 #2
    print("Result:",solve(A, k))