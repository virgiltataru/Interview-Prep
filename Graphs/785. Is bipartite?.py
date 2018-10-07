def isBipartite(self, graph):
    def dfs(v, cur_color):
        if v in color:
            return color[v] == cur_color
        color[v] = cur_color
        return all(dfs(w, cur_color ^ 1) for w in graph[v])
    color = {}
    return all(dfs(v, 0) for v in range(len(graph)) if v not in color)
