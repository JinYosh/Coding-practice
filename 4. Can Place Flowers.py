def solve(flowerbed, n):
    if n == 0:
        return True
    if len(flowerbed) == 1:
        if flowerbed[0] == 0 and n == 1:
            return True
        elif flowerbed[0] == 1 and n == 1:
            return False
        elif n > 1:
            return False
        else:
            return True
    elif len(flowerbed) == 2:
        if sum(flowerbed) < 1 and n == 1:
            return True
        else:
            return False
    else:
        i = 0
        while i < len(flowerbed):
            if flowerbed[i] == 0:
                if ((i - 1) > -1) and ((i + 1) <= len(flowerbed)):
                    if sum(flowerbed[i-1 : i+2]) == 0:
                        flowerbed[i] = 1
                        n -= 1
                elif i + 1 == len(flowerbed):
                    if sum(flowerbed[i-1:i+1]) == 0:
                        flowerbed[i] = 1
                        n -= 1
                elif i - 1 == -1:
                    if sum(flowerbed[i:i+2]) == 0:
                        flowerbed[i] = 1
                        n -= 1
            i += 1
            if n == 0:
                break
        if n == 0:
            return True
        return False
    
if __name__ == "__main__":
    flowerbed = [0,0,1,0,0]
    n = 1
    print("Result:",solve(flowerbed, n))