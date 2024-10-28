def amazingSub(A):
    vowels = ["A","a","E","e","I","i","O","o","U","u"]
    arr_size = len(A)
    total_sub_arr = 0
    for i in range(len(A)):
        if A[i] in vowels:
            total_sub_arr += arr_size - i
    return total_sub_arr % 10003

if __name__ == "__main__":
    A = "ABEC"
    print("Result:",amazingSub(A))