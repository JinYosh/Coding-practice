def secondLargest(A):
    largest = -1
    s_largest = -1
    for num in A:
        if largest < num:
            if s_largest < largest:
                s_largest = largest
            largest = num
        if s_largest < num and largest > num:
            s_largest = num
    return s_largest

if __name__ == "__main__":
    A = [2]
    print("Result:",secondLargest(A))