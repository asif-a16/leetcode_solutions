class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        parent = [i for i in range(n)]
        rank = [1] * n

        def find_parent(node):
            cur = node

            while cur != parent[cur]:
                parent[cur] = parent[parent[cur]]
                cur = parent[cur]
            return cur
        
        def union(node1, node2):
            parent1, parent2 = find_parent(node1), find_parent(node2)

            if parent1 == parent2:
                return 0
            
            if rank[parent2] > rank[parent1]:
                parent[parent1] = parent2
                rank[parent2] += rank[parent1]
            else:
                parent[parent2] = parent1
                rank[parent1] += rank[parent2]
            return 1
        
        result = n
        for node1, node2 in edges:
            result -= union(node1, node2)

        return result
