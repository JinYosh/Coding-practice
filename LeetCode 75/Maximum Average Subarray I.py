def findMaxAverage(nums, k):
    arr_size = len(nums)
    if arr_size < k:
        return False
    max_sum_avg = 0
    sum_ = 0
    sum_avg = 0
    for i in range(k):
        sum_ += nums[i]
    sum_avg = sum_ / k 
    max_sum_avg = sum_avg
    l = 0
    for i in range(k, arr_size, 1):
        sum_ -= nums[l]
        sum_ += nums[i]
        sum_avg = round(sum_ / k, 5)
        max_sum_avg = max(sum_avg, max_sum_avg)
        l += 1
    return max_sum_avg

if __name__ == "__main__":
    nums = [5]
    k = 1
    print("Result:",findMaxAverage(nums, k))