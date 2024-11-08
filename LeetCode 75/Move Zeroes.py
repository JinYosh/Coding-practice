def moveZeroes(nums):
    zero_i = -1
    i = 0
    while i < len(nums):
        if nums[i] == 0 and zero_i == -1:
            zero_i = i
        elif zero_i != -1 and nums[i] != 0:
            temp = nums[i]
            nums[i] = 0
            nums[zero_i] = temp
            zero_i += 1
        i += 1
    print(nums)
    
            

if __name__ == "__main__":
    nums = [0,1,0,3,12]
    moveZeroes(nums)
    print("Result",nums)