def solve(A, e_flower):
    prev = A[0]
    for i in range(1, len(A)):
        if prev == 0:
            e_flower -= 1
        prev = A[i]
    return True if e_flower == 0 else False

def solve1(flowerbed, n):
    fl_len = len(flowerbed)
    if n == 0:
        return True
    if fl_len == 1:
        if max(flowerbed) == 0:
            n -= 1
            return True if n == 0 else False
        else:
            return True if n == 0 else False
    elif fl_len == 2:
        if max(flowerbed) == 0:
            n -= 1
            return True if n == 0 else False
        else:
            return True if n == 0 else False
    
    index_1 = None
    index_2 = None
    index_3 = None
    index_2 = flowerbed[0]
    index_3 = flowerbed[1]
    flowerPlaced = False
    if max(index_2, index_3) == 0:
        n -= 1
        flowerPlaced = True
    i = 2
    while i < fl_len and n > 0:
        index_1 = index_2 if flowerPlaced == False else 1
        index_2 = index_3
        index_3 = flowerbed[i]
        flowerPlaced = False
        if index_1 == 0 and index_2 == 0 and index_3 == 0:
            n -= 1
            flowerPlaced = True
        i += 1
    index_1 = index_2 if flowerPlaced == False else 1
    index_2 = index_3
    if n > 0:
        if max(index_1, index_2) == 0:
            n -= 1
            flowerPlaced = True
    else:
        return True
    return True if n == 0 else False


if __name__ == "__main__":
    A = [0]
    e_flower = 0
    print("Result:",solve1(A, e_flower))
        

            
