def largestAltitude(gain):
    PS = [0] * (len(gain) + 1)
    for i in range(len(gain)):
        sum_ = PS[i] + gain[i]
        PS[i+1] = sum_
    return max(PS)
if __name__ == "__main__":
    gain = [-4,-3,-2,-1,4,3,2]
    print("Result:",largestAltitude(gain))
