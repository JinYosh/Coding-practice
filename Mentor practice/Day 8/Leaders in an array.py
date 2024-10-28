def leader(A):
    ans_list = []
    max_num = -(10 ** 9) + 7 
    for i in range(len(A)-1, -1, -1):
        if max_num < A[i]:
            max_num = A[i]
            ans_list.append(max_num)
    return ans_list

if __name__ == "__main__":
    A = [5,4]
    print("Result:",leader(A))
