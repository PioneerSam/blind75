'''
You are given an array of non-overlapping intervals intervals where intervals[i] = [starti, endi] represent the start and the end of the ith interval and intervals is sorted in ascending order by starti. You are also given an interval newInterval = [start, end] that represents the start and end of another interval.

Insert newInterval into intervals such that intervals is still sorted in ascending order by starti and intervals still does not have any overlapping intervals (merge overlapping intervals if necessary).

Return intervals after the insertion.

'''

class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        # we need to sort the intervals again haha
        # intervals.sort(key = lambda x:x[0])
        if not intervals:
            return [newInterval]

        new_left = newInterval[0]
        new_right = newInterval[1]

        result = []

        overlapped = False

        for interval in intervals:
            current_l = interval[0]
            current_r = interval[1]

            # completely before
            if current_r < new_left:
                result.append([current_l,current_r])
            # overlap
            elif current_r >= new_left and current_l <= new_right:
                new_left = min(current_l,new_left)
                new_right = max(current_r,new_right)
            # completely after
            elif current_l > new_right:
                if not overlapped:
                    result.append([new_left,new_right])
                    overlapped = True
                result.append([current_l,current_r])
            
            print("new left",new_left)
            print("new right,",new_right)
        
        if not overlapped:
            result.append([new_left,new_right])

        return result


                       
