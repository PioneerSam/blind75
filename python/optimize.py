'''
There are a total of numCourses courses you have to take, labeled from 0 to numCourses - 1. You are given an array prerequisites where prerequisites[i] = [ai, bi] indicates that you must take course bi first if you want to take course ai.

For example, the pair [0, 1], indicates that to take course 0 you have to first take course 1.
Return true if you can finish all courses. Otherwise, return false.
'''



class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = [[] for _ in range(numCourses)]

        state = [0 for _ in range(numCourses)]

        for pre in prerequisites:
            graph[pre[1]].append(pre[0])
        
        # # 1. iterative DFS
        # # 0 not visited, 1 is visiting, 2 is visited
        # stack = []

     
        # # True is entering, False is exiting
        # for i in range(numCourses):
        #     if state[i] == 0:
        #         stack.append((i,True))
        #         while stack:
        #             node_idx, flag = stack.pop()

        #             if flag:
        #                 if state[node_idx] == 1:
        #                     return False
        #                 elif state[node_idx] == 2:
        #                     continue
        #                 else:
        #                     state[node_idx] = 1
        #                     stack.append((node_idx,False))
        #                     # its neighbours
        #                     for nei in graph[node_idx]:
        #                         stack.append((nei,True))            
        #             else:
        #                 state[node_idx] = 2
        
        # return True

        ## 2. recursive DFS
        def dfs(node):
            if state[node] == 1:
                return True
            elif state[node] == 2:
                return False
            else:
                state[node] = 1
                for nei in graph[node]:
                   if dfs(nei):
                       return True
                state[node] = 2
                return False
                

        for i in range(numCourses):
            if state[i] == 2:
                continue
            ans = dfs(i)
            if ans:
                return False

        return True
                
        



                    
                
