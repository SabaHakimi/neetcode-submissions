class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # sounds like sliding window; consecutive characters, O(n) time, O(1) space
        # fixed size window?
        # permutation -> care about freqs
        # only lowercase letters -> O(26) space
        # list len 26, map chars to indices, values hold freq
        # use list comparison, constant time because O(26) worst case
        
        # Base case
        if len(s1) > len(s2):
            return False

        # Create s1 freqs
        s1_freqs = [0] * 26
        for c in s1:
            idx = ord(c) - ord('a')
            s1_freqs[idx] += 1

        # Initialize window
        l = 0
        r = len(s1) - 1
        s2_freqs = [0] * 26

        for i in range(r + 1):
            idx = ord(s2[i]) - ord('a')
            s2_freqs[idx] += 1

        print("s1_freqs", s1_freqs)
        print("s2_freqs", s2_freqs)
        # check match
        if s1_freqs == s2_freqs:
            return True

        # Slide window
        while r < len(s2) - 1:
            # slide over
            idx = ord(s2[l]) - ord('a')
            s2_freqs[idx] -= 1
            l += 1

            r += 1
            idx = ord(s2[r]) - ord('a')
            s2_freqs[idx] += 1

            print("s1_freqs", s1_freqs)
            print("s2_freqs", s2_freqs)

            # check match
            if s1_freqs == s2_freqs:
                return True
        
        return False


        