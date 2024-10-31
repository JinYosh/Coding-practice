def bulbs(A):
    count = 0 if A[0] == 1 else 1
    prev = A[0]
    for i in range(1, len(A)):
        if prev != A[i]:
            count += 1
        prev = A[i]
    return count

if __name__ == "__main__":
    A = [1,0,0,1]
    print("Result:",bulbs(A))
