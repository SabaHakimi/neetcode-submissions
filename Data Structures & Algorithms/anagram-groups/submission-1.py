class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # For each string: build alpha-counter array as hashmap key with idx as val
        anagramBank = {}
        i = 0
        for s in strs:
            char_c = [0] * 26
            for c in s:
                char_c[ord(c) - ord('a')] += 1
            
            key = tuple(char_c)
            print(key)
            if key in anagramBank:
                anagramBank[key].append(i)
            else:
                anagramBank[key] = [i]
            
            i += 1

        output = []
        for key in anagramBank:
            anagram_group = []
            for idx in anagramBank[key]:
                anagram_group.append(strs[idx])
            output.append(anagram_group)
        
        return output

    # relevant info: # of each char per string
    