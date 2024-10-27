def maxMinArray(a):
    min_ = 10 ** 9 
    max_ = -10 ** 9
    for num in a:
        max_ = max(max_, num)
        min_ = min(min_, num)
    return max_ + min_

if __name__ == "__main__":
    a = [-2, 1, -4, 5, 3]
    print("Result:",maxMinArray(a))