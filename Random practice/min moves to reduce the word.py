def solve(A):
    dic_ = {}
    for c in A:
        if c not in dic_.keys():
            dic_[c] = 1
        else:
            dic_[c] += 1
    min_moves = 0
    for k in dic_.keys():
        freq_ = dic_[k] 
        reduced = freq_ // 2
        min_moves += reduced
    return min_moves

if __name__ == "__main__":
    A = "baabacaa"
    print("Result:",solve(A))