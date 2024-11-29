def canVisitAllRooms(list_):
    total_rooms = len(list_)
    inital_keys = list_[0]
    list_[0] = "Unlocked"
    for key in inital_keys:
        unlock(list_ ,key)
    print(list_)
    for room in range(total_rooms):
        if list_[room] != "Unlocked":
            return False
    return True
        

def unlock(list_, key_):
    print("Key:{}, list: {}".format(key_, list_))
    if key_ != "Unlocked" and list_[key_] != "Unlocked":
        curr_keys = list_[key_]
        list_[key_] = "Unlocked"
        
        for key_ in curr_keys:
            unlock(list_, key_)


if __name__ == "__main__":
    rooms = [[1,3],[3,0,1],[2],[0]]
    print("Result:",canVisitAllRooms(rooms))

        
