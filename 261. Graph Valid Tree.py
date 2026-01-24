class ValHolder:
    def __init__(self, value: int):
        self.value = value

class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if not edges:
            return True
        
        graph = {}
        counter = 0
        graph_ids = []

        for node1, node2 in edges:
            if node1 == node2:
                return False
            if node1 not in graph and node2 not in graph:
                new_val = ValHolder(counter)
                graph[node1] = new_val
                graph[node2] = new_val
                graph_ids.append(new_val)
                counter += 1
            elif node1 in graph and node2 not in graph:
                graph[node2] = graph[node1]
            elif node1 not in graph and node2 in graph:
                graph[node1] = graph[node2]
            elif node1 in graph and node2 in graph and graph[node1].value != graph[node2].value:
                min_val = min(graph[node2].value, graph[node1].value)
                for id in graph_ids:
                    if id.value == graph[node2].value or id.value == graph[node1].value:
                        continue
                    id.value -= 1
                graph[node2].value = min_val
                graph[node1].value = min_val
                counter -= 1
            else:
                return False

        return counter == 1
