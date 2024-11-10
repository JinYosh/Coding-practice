def maxOperations(nums, k):
    HM = {}
    for i in range(len(nums)):
        if nums[i] in HM.keys():
            HM[nums[i]] += 1
        else:
            HM[nums[i]] = 1
    ops = 0
    for i in range(len(nums)):
        diff = k - nums[i]
        if diff in HM.keys():
            if HM[nums[i]] == 1:
                HM.pop(nums[i])
            else:
                HM[nums[i]] -= 1
            if diff in HM.keys():
                if HM[diff] == 1:
                    HM.pop(diff)
                else:
                    HM[diff] -= 1
            else:
                continue
            ops += 1
    return ops

if __name__ == "__main__":
    nums = [3,1,3,4,3]
    k = 6
    print("Result:",maxOperations(nums, k))