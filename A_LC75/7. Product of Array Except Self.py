def solve(nums):
    preProd = [0 for _ in range(len(nums))]
    sufProd = [0 for _ in range(len(nums))]
    preProd[0] = nums[0]
    sufProd[len(nums)-1] = nums[-1]
    i = 1
    while i < len(nums):
        preProd[i] = preProd[i-1] * nums[i]
        i += 1
    i = len(nums) - 2
    while i > -1:
        sufProd[i] = sufProd[i+1] * nums[i]
        i -= 1

    print(preProd, sufProd)
    ans_arr = []
    i = 0
    while i < len(nums):
        if i == 0:
            ans_arr.append(sufProd[i+1])
        elif i == len(nums) - 1:
            ans_arr.append(preProd[i-1])
        else:
            ans_arr.append(preProd[i-1] * sufProd[i+1])
        i += 1
    return ans_arr

if __name__ == "__main__":
    nums = [-1,1,0,-3,3]
    print("Result:",solve(nums))
