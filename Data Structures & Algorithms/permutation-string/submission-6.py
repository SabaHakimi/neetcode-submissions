class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # don't necessarily need info from both sides
        # sliding window over s2, valid when:
        # window exclusively contains characters in s1

        # only keep track of if valid; O(1) space
        # or dict of some kind
        # probably want dict for s1 for O(1) lookup
        # duplicate letters need to be acccounted for
        # remaining challenge is tracking window validity

        # to keep window valid:
        # iterate over array and if window valid:
            # return true if max value in dict is 0
            # bump right and update window vars
            # else bump left until window valid when invalid; if left exceeds right, bump right with it
            # when bumping right decrement s1 dict
            # when bumping left increment s1 dict

        # build s1 freqs
        freqs = {}
        for c in s1:
            if c in freqs:
                freqs[c] += 1
            else: freqs[c] = 1

        l = 0
        r = -1
        while r < len(s2) - 1:
            # if window valid
            if min(freqs.values()) >= 0:
                # win condition
                if max(freqs.values()) == 0:
                    return True

                # increment r and decrement new value
                r += 1
                if s2[r] in freqs:
                    freqs[s2[r]] -= 1
                else:
                    freqs[s2[r]] = -1
            else:
                # increment old val and bump string to make it valid
                while min(freqs.values()) < 0:
                    freqs[s2[l]] += 1
                    l += 1
        
        if min(freqs.values()) == 0 and max(freqs.values()) == 0:
            return True
        
        return False

        # a: 0
        # d: 0
        # c: 0

        # dcda

        # win = [cda]

