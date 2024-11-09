def maxArea1(heights):
    max_area = -float('inf')
    for i in range(len(heights)):
        area = 0
        for j in range(len(heights)):
            length = abs(j - i)
            height = min(heights[i], heights[j])
            area = length * height
            max_area = max(max_area, area)
    return max_area

def maxArea(heights):
    max_area = -float('inf')
    l = 0
    r = len(heights) - 1
    while l < r:
        length = r - l
        height = min(heights[l], heights[r])
        area = length * height
        max_area = max(area, max_area)
        if heights[l] < heights[r]:
            l += 1
        else:
            r -= 1

    return max_area
        



if __name__ == "__main__":
    heights = [1,2,4,3]
    #heights = [1,8,6,2,5,4,8,3,7]
    print("Result:",maxArea(heights))
