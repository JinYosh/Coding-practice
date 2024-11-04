def prodExceptSelf(A):
    if len(A) == 0:
        return []
    l_prod_list = [0] * len(A)
    r_prod_list = [0] * len(A)

    l_prod_list[0] = A[0]
    r_prod_list[-1] = A[-1]

    for i in range(1, len(A)):
        prod = l_prod_list[i - 1] * A[i]
        l_prod_list[i] = prod

    for i in range(len(A)-2, -1, -1):
        prod = r_prod_list[i + 1] * A[i]
        r_prod_list[i] = prod
    print(l_prod_list, r_prod_list)
    ans_list = [0] * len(A)
    for i in range(len(A)):
        l_prod = l_prod_list[i-1] if i-1 > -1 else 1
        r_prod = r_prod_list[i + 1] if i+1 < len(A) else 1
        prod = l_prod * r_prod
        ans_list[i] = prod
    return ans_list

if __name__ == "__main__":
    A = [1,2,3,4]
    print("Result:",prodExceptSelf(A))



