def countEleSort(a):
    a.sort()  # O(nlogn)
    count = 0
    i = len(a) - 1
    currNum = a[-1]
    while i > -1: # O(n)
        if currNum != a[i]:
            count += 1
        i -= 1
    return count

def countIterative(a):
    max_num = a[-1]
    count = 1
    for i in range(1, len(a)):
        if max_num == a[i]:
            count += 1
        elif max_num < a[i]:
            max_num = a[i]
            count = 1
    return len(a) - count

if __name__ == "__main__":
    a = [5, 5, 3]
    print("Result:",countIterative(a))

        
