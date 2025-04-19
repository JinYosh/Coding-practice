def rearrange(list_):
    def recur(incomplete, left_over, all_pos):
        if len(left_over) == 0:
            all_pos.append(incomplete)
        for i in range(len(left_over)):
            temp = left_over[:]
            incomplete += left_over.pop(i)
            recur(incomplete, left_over[:], all_pos)
            incomplete = incomplete[:-1]
            left_over = temp[:]
                
    incomplete = ""
    all_pos = []
    left_over = list_[:]
    recur(incomplete, left_over, all_pos)
    return all_pos

if __name__ =="__main__":
    list_ = ['a', 'b', 'c']
    print("Result:",rearrange(list_))