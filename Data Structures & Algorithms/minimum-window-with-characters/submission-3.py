class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # t can be longer than s
        # aim for O(n) time O(m) space
        # sliding window, dynamic size
        # probably maintain a freq list
        # window is valid when all chars in t are within window
        # shrink when window valid until it isn't, recording smallest valid window, then expand
        # concern is with shrinking preemptively, are we potentially missing ideal windows
        # is it possible for a character to be removed from window and excluded from a potential best match?
        # the smallest possible valid window that contains the leftmost incldued necessary character is already captured
        # ^ this invariant guarantees our solution
        
        # what info do we need to track?
        # we only need freq list for t, 
        # don't want to do exact match just make sure vals above 0

        # solution
        # build freq list for t

        # Base case
        if len(t) > len(s):
            return ""

        # Build freq mask
        freqs = {}
        for c in t:
            if c in freqs:
                freqs[c] -= 1
            else:
                freqs[c] = -1
        
        # Sliding window
        l = 0
        r = 0
        best_l = 0
        best_r = 1001

        while r < len(s):
            # Expand until valid window
            while r < len(s) and min(freqs.values()) < 0:
                if s[r] in freqs:
                    freqs[s[r]] += 1
                r += 1
            
            # Shrink till minimum valid window
            while min(freqs.values()) >= 0:
                # Update best window
                if r - l < best_r - best_l:
                    best_r = r
                    best_l = l

                # Shrink
                if s[l] in freqs:
                    freqs[s[l]] -= 1
                l += 1
        
        # Return smallest window
        if best_r != 1001:
            return s[best_l:best_r]
        return ""

        # freqs = {
        #     X: 0
        #     Y: 0
        #     Z: -1
        # }
                    
        # Input: s = "OUZODYXAZV", t = "XYZ"

        # Output: "YXAZ"