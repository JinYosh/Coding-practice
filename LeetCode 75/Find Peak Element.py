def findPeakElement(nums):
    peak_list = []
    def recursionBS(list_):
        L = 0
        R = len(list_) - 1
        if len(peak_list) > 1:
            return peak_list[0]
        while L <= R:
            mid = (L + R) // 2
            if mid - 1 > 0:
                if mid + 1 < len(list_):
                    if list_[mid - 1] < list_[mid] and list_[mid] > list_[mid + 1]:
                        peak_list.append(mid)
                else:
                    if list_[mid - 1] < list_[mid]:
                        peak_list.append(mid)
            else:
                if list_[mid] > list_[mid + 1]:
                    peak_list.append(mid)
                    
            


def findPeakElement1(nums):
    if len(nums) == 1:
        return 0
    peak_list = []
    for i in range(len(nums)):
        if i - 1 > -1:
            if i + 1 < len(nums):
                if nums[i-1] < nums[i] and nums[i] > nums[i+1]:
                    peak_list.append(i)
            else:
                if nums[i-1] < nums[i]:
                    peak_list.append(i)
        else:
            if nums[i] > nums[i+1]:
                peak_list.append(i)
    return peak_list

if __name__ == "__main__":
    nums = [1,2]#[1,2,3,1]
    print("Result:",findPeakElement(nums))

