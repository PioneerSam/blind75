#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    int characterReplacement(string s, int k) {
        int n = (int)s.size();
        if (k >= n) return n;

        vector<int> freq(26, 0);
        int l = 0;
        int maxFreq = 0;     // rolling max frequency in current/seen window
        int best = 0;

        for (int r = 0; r < n; ++r) {
            int idxR = s[r] - 'A';
            freq[idxR]++;
            maxFreq = max(maxFreq, freq[idxR]);

            // Shrink while invalid
            while ((r - l + 1) - maxFreq > k) {
                int idxL = s[l] - 'A';
                freq[idxL]--;
                l++;
            }

            best = max(best, r - l + 1);
        }

        return best;
    }
};
