class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # sliding window
        # hash table
        ss_chars = set()
        l = 0
        r = 0
        ll_ss = 0


        while r < len(s):
            while s[r] in ss_chars:
                ss_chars.remove(s[l])
                l += 1
            ss_chars.add(s[r])
            r += 1

            if len(ss_chars) > ll_ss:
                ll_ss = len(ss_chars)
        
        return ll_ss
        