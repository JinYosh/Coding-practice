def longestOnes(nums, k):
    max_ones = 0
    ones_ = 0
    zeroes = 0
    r = 0
    l = 0
    while r < len(nums): #nums = [1,1,1,0,0,0,1,1,1,1,0]
        num = nums[r]
        if num == 1:
            ones_ += 1
        elif num == 0:
            zeroes += 1
        
        if zeroes > k:
            last_num = nums[l]
            if last_num == 1:
                ones_ -= 1
            else:
                zeroes -= 1
            l += 1
        
        if zeroes <= k:
            max_ones = max(max_ones, ones_ + zeroes)
        r += 1
        
    return max_ones

if __name__ == "__main__":
    #nums = [1,1,1,0,0,0,1,1,1,1,0]
    nums = [0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1]
    k = 3
    print("Result:",longestOnes(nums, k))
