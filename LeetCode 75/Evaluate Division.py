def calcequation(equations, values, queries):
    def dfs(src, dest, adj, product, ans, visited):
        if src in visited:
            return ans
        if src == dest:
            ans = product
            return ans
        visited.append(src)
        for point, value in adj[src]:
            ans = dfs(point, dest, adj, product * value, ans, visited)
            if point == dest:
                break
        
        return ans    
        
    adj = {}
    nodes = set()
    for u, v in equations:
        adj[u] = []
        adj[v] = []
        nodes.add(u)
        nodes.add(v)
    
    i = 0
    while i < len(equations):
        u, v = equations[i]
        adj[u].append([v, values[i]])
        adj[v].append([u, 1/values[i]])
        i += 1
    
    print(adj)
    cal_list = []
    for src, dest in queries:
        product = 1
        ans = -1
        if (src in nodes) and (dest in nodes):
            visited = []
            ans = dfs(src, dest, adj, product, ans, visited)
        cal_list.append(ans)
    return cal_list


#def calcequation1(equations, values, queries):
#    def dfs(u, v, adj, visited):
#        visited.append(u)
#        cal_val = -1
#        for a, val in adj[u]:
#            if a == v or a == u:
#                return val
#            elif a in visited:
#                continue
#            cal_val = val * dfs(a, v, adj, visited)
#            if cal_val > 0:
#                break
#        return cal_val
#
#    adj = {}
#    i = 0
#    nodes = set()
#    for u, v in equations:
#        adj[u] = []
#        adj[v] = []
#        nodes.add(u)
#        nodes.add(v)
#    while i < len(equations):
#        u, v = equations[i]
#        wt = values[i]
#        
#        adj[u].append([v, wt])
#        adj[v].append([u, 1/wt])
#
#        i += 1
#    print(adj)
#    cal_list = []
#    for u, v in queries:
#        if u not in nodes or v not in nodes:
#            cal_list.append(-1)
#        elif u == v:
#            cal_list.append(1)
#        else:
#            wt = dfs(u, v, adj, [])
#            cal_list.append(wt if wt > 0 else -1)
#
#    return cal_list
    
    
if __name__ == "__main__":
    equations = [["x1","x2"],["x2","x3"],["x3","x4"],["x4","x5"]]
    values = [3.0,4.0,5.0,6.0]
    queries = [["x1","x5"],["x5","x2"],["x2","x4"],["x2","x2"],["x2","x9"],["x9","x9"]]
    # Expected -> [360.00000,0.00833,20.00000,1.00000,-1.00000,-1.00000]
    print("Result:",calcequation(equations, values, queries))

#
#{'x1': [['x2', 3.0]],
#  'x2': [['x1', 0.3333333333333333], ['x3', 4.0]],
#  'x3': [['x2', 0.25], ['x4', 5.0]],
#  'x4': [['x3', 0.2], ['x5', 6.0]],
#  'x5': [['x4', 0.16666666666666666]]
#}

