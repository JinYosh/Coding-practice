def calcequation(equations, values, queries):
    def dfs(u, v, adj, visited):
        visited.append(u)
        cal_val = -1
        for a, val in adj[u]:
            if a == v or a == u:
                return val
            elif a in visited:
                continue
            cal_val = val * dfs(a, v, adj, visited)
            if cal_val > 0:
                break
        return cal_val

    adj = {}
    i = 0
    nodes = set()
    for u, v in equations:
        adj[u] = []
        adj[v] = []
        nodes.add(u)
        nodes.add(v)
    while i < len(equations):
        u, v = equations[i]
        wt = values[i]
        
        adj[u].append([v, wt])
        adj[v].append([u, 1/wt])

        i += 1
    print(adj)
    cal_list = []
    for u, v in queries:
        if u not in nodes or v not in nodes:
            cal_list.append(-1)
        elif u == v:
            cal_list.append(1)
        else:
            wt = dfs(u, v, adj, [])
            cal_list.append(wt if wt > 0 else -1)
    return cal_list
    
    
if __name__ == "__main__":
    equations = [["x1","x2"],["x2","x3"],["x1","x4"],["x2","x5"]]
    values = [3.0,0.5,3.4,5.6]
    queries = [["x2","x4"],["x1","x5"],["x1","x3"],["x5","x5"],["x5","x1"],["x3","x4"],["x4","x3"],["x6","x6"],["x0","x0"]]
    print("Result:",calcequation(equations, values, queries))

#
#{'x1': [['x2', 3.0], ['x4', 3.4]],
# 'x2': [['x1', 0.3333333333333333],
#        ['x3', 0.5], ['x5', 5.6]],
# 'x3': [['x2', 2.0]], 
# 'x4': [['x1', 0.29411764705882354]],
# 'x5': [['x2', 0.17857142857142858]]
#}
