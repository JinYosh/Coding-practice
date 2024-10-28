def subSeqBF(A):
    count = 0
    for i in range(len(A)):
        count_g = 0
        if A[i] == "A":
            for j in range(i + 1, len(A)):
                if A[j] == "G":
                    count_g += 1
        count += count_g
    return count

def subSeqCarryForward(A):
    count = 0
    count_A = 0
    for i in range(len(A)):
        if A[i] == "A":
            count_A += 1
        elif A[i] == "G":
            count += count_A
    return count % ((10 ** 9) + 7)


if __name__ == "__main__":
    A = "ABCGAG"
    print("Result:",subSeqBF(A))