class Solution:

        # ["hello", "leg", "bar", "bob"]
        # ["5hello3leg3bar3bob"]
    def encode(self, strs: List[str]) -> str:
        encoded_str = []
        for s in strs:
            encoded_str.append(str(len(s)))
            encoded_str.append('#')
            encoded_str.append(s)
        
        return "".join(encoded_str)


    #["5#hello3#leg3#bar3#bob"]
    def decode(self, s: str) -> List[str]:
        decoded_strs = []
        i = 0

        while i < len(s):
            j = i
            while s[j] != '#':
                j += 1
            
            str_len = int(s[i:j]) 

            i = j + 1
            decoded_strs.append(s[i:(i + str_len)])

            i = i + str_len

        
        return decoded_strs
            