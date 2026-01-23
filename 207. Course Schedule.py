from collections import defaultdict
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        if not prerequisites:
            return True
        
        pre_map = defaultdict(list)
        for a, b in prerequisites:
            pre_map[a].append(b)

        visited = set()

        def dfs(course: int):
            if course in visited:
                return False
            if pre_map[course] == []:
                return True
            
            visited.add(course)
            
            for pre in pre_map[course]:
                if not dfs(pre): return False

            visited.remove(course)
            pre_map[course] = []

            return True
        
        for course in range(numCourses):
            if not dfs(course): return False

        return True
