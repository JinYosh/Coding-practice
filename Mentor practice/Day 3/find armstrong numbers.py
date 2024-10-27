def armstrongNum(num):
    temp = num
    armstr = 0
    while temp > 0:
        rem = temp % 10
        temp = temp // 10
        armstr += (rem ** 3)
    if armstr == num:
        return True
    return False

def listArmstrongNum(a):
    ansList = []
    for num in range(1, a):
        isArm = armstrongNum(num)
        if isArm:
            ansList.append(num)
    return ansList

if __name__ == "__main__":
    a = 200
    print("Result:",listArmstrongNum(a))
