class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        graph={i:[]for i in range(numCourses)}
        for a,b in prerequisites:
            graph[a].append(b)
        visit=[0]*numCourses
        def dfs(course):
            if visit[course]==1:
                return False
            if visit[course]==2:
                return True
            visit[course]=1
            for pre in graph[course]:
                if not dfs(pre):
                    return False
            visit[course]=2
            return True
        for i in range(numCourses):
            if not dfs(i):
                return False
        return True
