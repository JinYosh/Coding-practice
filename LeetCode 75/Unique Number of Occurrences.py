def uniqueOccurrences(nums):
    HM = {}
    for num in nums:
        if num in HM.keys():
            HM[num] += 1
        else:
            HM[num] = 1
    list_ = []
    for key in HM.keys():
        list_.append(HM[key])
    if len(set(list_)) != len(list_):
        return False
    return True

if __name__ == "__main__":
    nums = [1,2]
    print("Result:",uniqueOccurrences(nums))