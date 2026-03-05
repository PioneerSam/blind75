#include <algorithm>
#include <vector>


class Solution {
public:
    int maxSubArray(vector<int>& nums) {

    if(nums.size() == 1){
        return nums[0];
    }

    int rolling_sum = nums[0];
    int max_sum = nums[0];

    for(int i=0;i < nums.size();i++){
        rolling_sum = std::max(rolling_sum + nums[i],nums[i]);

        max_sum = std::max(rolling_sum,max_sum);
    }

    return max_sum;


        
    }
};