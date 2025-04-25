def solve(candies, extraCandies):
    max_num = max(candies)
    result_list = []
    for candy in candies:
        if candy + extraCandies >= max_num:
            result_list.append(True)
        else:
            result_list.append(False)
    return result_list

if __name__ == "__main__":
    candies = [12,1,12]
    extraCandies = 10
    print("Result:",solve(candies, extraCandies))