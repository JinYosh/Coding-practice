def pivotIndex(nums):
    PS = [nums[0]]
    for i in range(1, len(nums)):
        PS.append(PS[i-1] + nums[i])
    for i in range(len(nums)):
        l_sum = PS[i-1] if i-1 > -1 else 0
        r_sum = PS[-1] - PS[i]
        if l_sum == r_sum:
            return i
    return -1

if __name__ == "__main__":
    nums = [2,1,-1]
    print("Result:",pivotIndex(nums)) 
