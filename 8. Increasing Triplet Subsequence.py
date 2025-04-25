def solve(nums):
    #for j in range(1, len(nums)-1, 1):
    #    for i in range(j-1, -1, -1):
    #        for k in range(j+1, len(nums), 1):
    #            if nums[i] < nums[j] < nums[k]:
    #                return True
    #return False
    min_from_left = [None for _ in range(len(nums))]
    max_from_right = [None for _ in range(len(nums))]
    min_ = None
    for i in range(len(nums)):
        if min_ == None or min_ > nums[i]:
            min_ = nums[i]
        min_from_left[i] = min_
    max_ = None
    for i in range(len(nums) - 1, -1, -1):
        if max_ == None or max_ < nums[i]:
            max_ = nums[i]
        max_from_right[i] = max_
    
    i = 1
    while i < len(nums) - 1:
        if min_from_left[i-1] < nums[i] and nums[i] < max_from_right[i]:
            return True
        i += 1
    return False

if __name__ == "__main__":
    nums = [5,4,3,2,1]#[2,1,5,0,4,6]
    print("Result:",solve(nums))