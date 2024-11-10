def findDifferences(nums1, nums2):
    set_nums1 = set(nums1)
    set_nums2 = set(nums2)
    
    dist1 = []
    dist2 = []

    for num in set_nums1:
        if num not in set_nums2:
            dist1.append(num)
    for num in set_nums2:
        if num not in set_nums1:
            dist2.append(num)
    return [dist1,dist2]

if __name__ == "__main__":
    nums1 = [1,2,3,3]
    nums2 = [1,1,2,2]
    print("Result:",findDifferences(nums1, nums2))

    
