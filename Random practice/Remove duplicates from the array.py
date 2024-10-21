def removeDupBF(arr):
    ans_list = []
    i = 0
    while i < len(arr):
        j = i - 1
        dupFound = False
        # check only the left side of the array
        while j > -1:
            if arr[i] == arr[j]:
                dupFound = True
                break
            j -= 1
        if not dupFound:
            ans_list.append(arr[i])
        i += 1
    return ans_list

def removeDupHS(arr):
    set_ = set()
    for num in arr:
        set_.add(num)
    return list(set_)
        

if __name__ == "__main__":
    A = [1,2,3,2,3]
    print("Result:",removeDupHS(A))
