class Solution:
    def countSubstrings(self, s: str) -> int:
        palindrome_count = 0
        for i in range(len(s)):
            palindrome_count += self.count_palindromes(s, i, i)
            palindrome_count += self.count_palindromes(s, i, i + 1)
        return palindrome_count

    def count_palindromes(self, s, l, r) -> int:
        count = 0
        end = len(s)
        while l >= 0 and r < end and s[l] == s[r]:
            count += 1
            r += 1
            l -= 1
        return count 

        # Example
        # r a c e c a r  t  o  o  t
        # 1 2 3 7 8 9 10 11 14 15 16
        # ans -> 16

        # a a a
        # 2 5 6

        # very expensive to consider every substring
        # goal is idnmost efficient way to preliminarily determine if palindrome
        # current thought:
        # scan left to right (for each char in string):
        #   if current substring palindrome:
        #       counter += 1
        #       
        # notes:
        # - careful with Index out of bounds
        # - consider odd & even palindromes before skip to next char (2 fails in a row)