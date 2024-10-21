def reverseArray(arr):
    start_ = 0
    end_ = len(arr) - 1
    while start_ < end_:
        temp = arr[start_]
        arr[start_] = arr[end_]
        arr[end_] = temp
        start_ += 1
        end_ -= 1

if __name__ == "__main__":
    A = [1,2,3,4]
    print("Result:",reverseArray(A))
    print(A)