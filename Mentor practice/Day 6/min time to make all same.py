def timeEqualityBF(A):
    min_time = 10 ** 9 
    time = 0
    for i in range(len(A)):
        time = 0
        for j in range(len(A)):
            if j != i and A[i] != A[j]:
                time += 1
        min_time = min(time, min_time)
    return min_time

def timeEqualityMaxFreq(A):
    HM = {}
    for num in A:
        if num in HM.keys():
            HM[num] += 1
        else:
            HM[num] = 1
    max_freq = 0
    for num in HM.keys():
        freq = HM[num]
        if freq > max_freq:
            max_freq = freq
    min_time = len(A) - max_freq
    return min_time

def timeEqualitySort(A):
    A.sort()
    maxFreq = 0
    num = A[0]
    freq = 0
    for i in range(len(A)):
        if A[i] == num:
            freq += 1
        elif A[i] != num:
            num = A[i]
            freq = 1
        maxFreq = max(maxFreq, freq)
    return len(A) - maxFreq
            


if __name__ == "__main__":
    A = [1,2,2,3,1,1]
    print("Result:",timeEqualityBF(A))


