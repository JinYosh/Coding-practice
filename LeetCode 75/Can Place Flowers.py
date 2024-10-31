def solve(A, e_flower):
    prev = A[0]
    for i in range(1, len(A)):
        if prev == 0:
            e_flower -= 1
        prev = A[i]
    return True if e_flower == 0 else False

def solve1(A, e_flower):
    if len(A) == 1:
        if A[0] == 0:
            e_flower -= 1
            return True if e_flower == 0 else False
        else:
            return True if e_flower == 0 else False
    elif len(A) == 2:
        if max(A) == 1:
            return True if e_flower == 0 else False
        else:
            e_flower -= 1
            return True if e_flower == 0 else False
    
    index_1 = None
    index_2 = None
    index_3 = None

    index_3 = A[1]
    index_2 = A[0]

    if max(A[:2]) != 1:
        e_flower -= 1
        index_1 = 1
    else:
        index_1 = index_2
    index_2 = index_3
    index_3 = A[2]

    if e_flower > 0:
        if index_1 == 0 and index_2 == 0 and index_3 == 0:
            e_flower -= 1
    else:
        return True
    flowerSet = False
    for i in range(3, len(A)):
        index_1 = index_2 if flowerSet == False else 1
        index_2 = index_3
        index_3 = A[i]
        if e_flower > 0:
            if index_1 == 0 and index_2 == 0 and index_3 == 0:
                e_flower -= 1
                flowerSet = True
            else:
                flowerSet = False
        else:
            return True

    if e_flower > 0:
        index_1 = index_2 if flowerSet == False else 1
        index_2 = index_3
        if index_1 == 0 and index_2 == 0:
            e_flower -= 1
    else:
        return True
    
    return True if e_flower == 0 else False

if __name__ == "__main__":
    A = [1,0,0,0,1]
    e_flower = 2
    print("Result:",solve1(A, e_flower))
        

            
