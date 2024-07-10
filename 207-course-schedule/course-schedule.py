class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        preMap = {i: [] for i in range(numCourses)}

        # map each course to : prereq list
        for crs, pre in prerequisites:
            preMap[crs].append(pre)

        visiting = set()
        visited = set()  # memoization to store the results of already visited courses

        def dfs(crs):
            if crs in visiting:
                return False  # cycle detected
            if crs in visited:
                return True  # already visited and no cycle

            visiting.add(crs)
            for pre in preMap[crs]:
                if not dfs(pre):
                    return False
            visiting.remove(crs)
            visited.add(crs)
            return True

        for c in range(numCourses):
            if not dfs(c):
                return False
        return True