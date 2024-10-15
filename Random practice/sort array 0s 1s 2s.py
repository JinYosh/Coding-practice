def solve(A):
    z_count = 0
    o_count = 0
    t_count = 0
    for num in A:
        if num == 0:
            z_count += 1
        elif num == 1:
            o_count += 1
        else:
            t_count += 1
    return [0]*z_count + [1]*o_count + [2]*t_count

if __name__ == "__main__":
    A = [0,1,2,0,1,2]
    print("Result:",solve(A))