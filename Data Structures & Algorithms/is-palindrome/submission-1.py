class Solution:
    def isPalindrome(self, s: str) -> bool:
        clean_str = ''.join(char for char in s if char.isalnum()).lower()
        str_len = len(clean_str)
        j = str_len - 1
        for i in range(str_len // 2):
            if (clean_str[i] != clean_str[j]):
                return False
            j -= 1
        return True