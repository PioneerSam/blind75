#include <algorithm>
#include <vector>


class Solution {
public:
    bool exist(vector<vector<char>>& board, string word) {
        
        int n = board.size();
        int m = board[0].size();

        int d = word.size();



        function<bool(int,int,int)> dfs = [&](int r, int c, int idx) {

            if (!(0<=r && r< n && 0<=c && c<m)){
                return false;
            }

            if(board[r][c] == '#'){
                return false;
            }

            
            if(board[r][c] == word[idx]){
                if(idx == d-1){
                    return true;
                }
                char temp = board[r][c];
                board[r][c] = '#';
                vector<pair<int,int>> dirs = {{1,0},{-1,0},{0,1},{0,-1}};

                for(auto &p:dirs){
                    int nr = r + p.first;
                    int nc = c + p.second;
                    if(idx+1 < d){
                        if(dfs(nr,nc,idx+1)){
                            return true;
                        }
                    }
                }
                board[r][c] = temp;
                return false;
            }else{
                return false;
            }
        };

        for(int i=0; i<n;i++){
            for(int j=0; j<m; j++){
                bool ans = dfs(i,j,0);
                if(ans){
                    return true;
                }
            }
        }
        return false;
    }
};