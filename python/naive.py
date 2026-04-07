'''
There are a total of numCourses courses you have to take, labeled from 0 to numCourses - 1. You are given an array prerequisites where prerequisites[i] = [ai, bi] indicates that you must take course bi first if you want to take course ai.

For example, the pair [0, 1], indicates that to take course 0 you have to first take course 1.
Return true if you can finish all courses. Otherwise, return false.
'''



class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # So [1,0] means in order to take 1 you have to take 0 first 
        # somehow it is detecting a cycle lol
        # lets do it naively

        # we need to see how many courses there are
        # ok we need to create a adjancancy list

        graph = [[] for _ in range(numCourses)]
        indegree = [0 for _ in range(numCourses)]
        taken = 0

        for pre in prerequisites:
            graph[pre[1]].append(pre[0])
            indegree[pre[0]] += 1

        print("the adjanency list is:",graph)

        # the indegree array
        print("the indegree array is:",indegree)

        # remove courses with indegree 0
        from collections import deque

        q = deque()

        for node_idx in range(numCourses):
            if indegree[node_idx] == 0:
                q.append(node_idx)


        while q:
            cur = q.popleft()
            taken += 1

            # drop the indegree of its neigbours
            for node_idx in graph[cur]:
                indegree[node_idx] -=1
                if indegree[node_idx] == 0:
                    q.append(node_idx)

        
        return taken == numCourses


            



                       
