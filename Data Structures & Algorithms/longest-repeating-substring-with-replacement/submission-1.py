class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # sliding window
        # all chars within window are relevant info
        # don't track just one at a time
        # dict
        # window is valid when (w/ replacements) there is only one char
        # l and r will keep track of total chars
        # when window invalid, shrink from left until valid
        # this requires repeatedly retrieving the current most frequent character

        counts = {}
        l = 0
        r = 0 
        max_win = 0
        max_freq = 0 
        win_size = 0 

        while r < len(s):  
            # expand window
            if s[r] in counts:
                counts[s[r]] += 1
            else:
                counts[s[r]] = 1
            r += 1 

            # recompute
            max_freq = max(counts.values())
            win_size = r - l

            # if window still valid
            if win_size - max_freq <= k:
                # update max
                if win_size > max_win:
                    max_win = win_size
            else:
                # shrink window
                counts[s[l]] -= 1
                l += 1

        return max_win
     
