def longestSubarray(nums):
    max_ones = 0
    ones_ = 0
    zeroes = 0
    l = 0
    r = 0
    k = 1
    while r < len(nums):
        num = nums[r]
        if num == 1:
            ones_ += 1
        else:
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
    ans_list = [1 for _ in range(max_ones -1)]
    if ans_list == []:
        return 0
    return ans_list

if __name__ == "__main__":
    nums = [1,1,0,0,1]
    print("Result:",longestSubarray(nums))
