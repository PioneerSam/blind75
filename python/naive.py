'''
Given an array of intervals where intervals[i] = [starti, endi], merge all overlapping intervals, and return an array of the non-overlapping intervals that cover all the intervals in the input.

 

Example 1:

Input: intervals = [[1,3],[2,6],[8,10],[15,18]]
Output: [[1,6],[8,10],[15,18]]
Explanation: Since intervals [1,3] and [2,6] overlap, merge them into [1,6].
Example 2:

Input: intervals = [[1,4],[4,5]]
Output: [[1,5]]
Explanation: Intervals [1,4] and [4,5] are considered overlapping.
Example 3:

Input: intervals = [[4,7],[1,4]]
Output: [[1,7]]
Explanation: Intervals [1,4] and [4,7] are considered overlapping.

'''

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # I think it is greedy again
        result = []

        if not intervals:
            return result
        # I need to sort the intervals based on end 
        intervals = sorted(intervals,key = lambda x:x[0])
        current_min_l = intervals[0][0]
        current_max_r = intervals[0][1]

        for interval in intervals[1::]:
            print("current_min_l", current_min_l)
            print("current max r",current_max_r)
            current_l = interval[0]
            current_r = interval[1]

            if current_l <= current_max_r:
                current_min_l = min(current_min_l,current_l)
                current_max_r = max(current_max_r,current_r)
            else:
                # we need to start another one
                result.append([current_min_l,current_max_r])

                current_min_l = current_l
                current_max_r = current_r
        
        result.append([current_min_l,current_max_r])
        return result
                       
