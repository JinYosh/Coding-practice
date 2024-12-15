import heapq
def totalCost(costs, k, candidates):
    h1 = []
    h2 = []
    L1 = 0
    L2 = len(costs)
    for L1 in range(candidates):
        if L1 == len(costs):
            L1 -= 1
            break
        heapq.heappush(h1, costs[L1])
        #costs[i] == None
    
    if L1 < len(costs):
        L2_len = 0
        for L2 in range(len(costs)-1, L1, -1):
            if L2_len == candidates:
                L2 += 1
                break
            heapq.heappush(h2, costs[L2])
            L2_len += 1
        

    
    t_Cost = 0
    for _ in range(k):
        if len(h1) > 0 and len(h2) > 0:
            if h1[0] <= h2[0]:
                t_Cost += heapq.heappop(h1)
                if L1 + 1 < L2:
                    heapq.heappush(h1, costs[L1 + 1])
                    L1 += 1
            else:
                t_Cost += heapq.heappop(h2)
                if L2 - 1 > L1:
                    heapq.heappush(h2, costs[L2 - 1])
                    L2 -= 1
        else:
            if len(h1) > 0:
                t_Cost += heapq.heappop(h1)
            elif len(h2) > 0:
                t_Cost += heapq.heappop(h2)
            else:
                break
    return t_Cost

if __name__ == "__main__":
    costs = [31,25,72,79,74,65,84,91,18,59,27,9,81,33,17,58]
    k = 11
    candidates = 2
    print("Result:",totalCost(costs, k, candidates))


    