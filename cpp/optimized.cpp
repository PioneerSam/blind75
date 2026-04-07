#include <algorithm>
#include <vector>
#include <queue>


class Solution {
public:
    bool canFinish(int numCourses, vector<vector<int>>& prerequisites) {
        // we need to do iterative BFS toposort
        // we need to build the graph where it is a list of lists
        vector<vector<int>> graph(numCourses);
        // indegree list
        vector<int> indegree(numCourses);

        int count_taken = 0;

        for(int i = 0; i < prerequisites.size();i++){
            vector<int> pre = prerequisites[i];
            graph[pre[1]].push_back(pre[0]);
            indegree[pre[0]]++;
        }
        std::queue<int> q;

        for(int i=0;i<numCourses;i++){
            if(indegree[i] == 0){
                q.push(i);
            }
        }

        while(!q.empty()){
            int node = q.front();
            q.pop();
            
            count_taken++;

            for(int j = 0; j<graph[node].size();j++){
                int nei = graph[node][j];
                indegree[nei]--;

                if(indegree[nei] == 0){
                    q.push(nei);
                }

            }        

        }

        return count_taken == numCourses; 
    }
};