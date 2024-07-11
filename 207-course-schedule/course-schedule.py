class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        premap = {i: [] for i in range(numCourses)}

        for cr, pre in prerequisites:
            premap[cr].append(pre)
        
        visited = set()
        visiting = set()
        def dfs(cr):
            if cr in visiting:
                return False
            if cr in visited:
                return True
            
            visiting.add(cr)

            for pre in premap[cr]:
                if not dfs(pre):
                    return False
            visiting.remove(cr)
            visited.add(cr)
            return True
        for i in range(numCourses):
            if not dfs(i):
                return False
        return True
            
