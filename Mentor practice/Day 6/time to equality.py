def timeEqualityMax(A):
    max_ = -((10 ** 9) + 7)
    for num in A:
        max_ = max(num, max_)
    sec_req = 0
    for num in A:
        sec_req += (max_ - num)
    return sec_req

if __name__ == "__main__":
    A = [2,4,1,3,2]
    print("Result:",timeEqualityMax(A))