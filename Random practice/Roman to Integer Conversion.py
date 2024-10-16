def solve(A):
    num = 0
    dict_ = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M':1000}
    if len(A) == 1:
        return dict_[A[0]]
    index = 0
    while index < len(A):
        a = A[index]
        if index + 1 < len(A):
            b = A[index + 1] 
            rom1 = dict_[a]
            rom2 = dict_[b]
            if rom1 > rom2:
                num += rom1
                index += 1
            elif rom1 < rom2:
                num += (rom2 - rom1)
                index += 2
            else:
                num += (rom1 + rom2) 
                index += 2
        else:
            rom1 = dict_[a]
            num += rom1
            index += 1
        print(num, index, end=" ")
    return num

if __name__ == "__main__":
    A = "MCMXCIV"#"MCDLXXVI" #"MCMIV"
    print("Result:",solve(A))
    
    
