'''
You are given a string s and an integer k. You can choose any character of the string and change it to any other uppercase English character. You can perform this operation at most k times.

Return the length of the longest substring containing the same letter you can get after performing the above operations.
'''



class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # you know what lets take a dp approach
        # every array of integer records the longest string so far
        # isnt k is the window size
        n = len(s)

        if n <= k:
            return n
        

        l = 0
        freq = [0] * 26
        max_window_size = 0
        
        for r in range(0,n,1):
            window_size = r - l + 1

            id_r =  ord(s[r]) - ord("A")
            freq[id_r] += 1
            max_freq = max(freq)

            while(r-l+1 - max_freq > k):
                id_l = ord(s[l]) - ord("A")
                freq[id_l] -= 1
                l+=1
            window_size = r - l + 1
        
            if window_size > max_window_size:
                max_window_size = window_size

        return max_window_size






