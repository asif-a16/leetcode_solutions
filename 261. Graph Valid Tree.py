class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if not n:
            return True
        
        adj = { i:[] for i in range(n)}

        for node1, node2 in edges:
            adj[node1].append(node2)
            adj[node2].append(node1)

        visited = set()
        def dfs(node, prev_node):
            if node in visited:
                return False
            
            visited.add(node)
            for neighbour_node in adj[node]:
                if neighbour_node == prev_node:
                    continue
                if not dfs(neighbour_node, node):
                    return False
                
            return True
        
        return dfs(0, -1) and len(visited) == n
