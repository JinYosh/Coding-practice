def solve(nums):
    if len(nums) == 1:
        return None
    arr_size = len(nums)
    z_count = 0
    z_i = 0
    for _ in range(arr_size):
        if nums[z_i] == 0:
            z_count += 1
            nums.pop(z_i)
        else:
            z_i += 1
    for i in range(z_count):
        nums.append(0)


if __name__ == "__main__":
    nums = [1,0,0,1,1]
    solve(nums)
    print("Result:",nums)
