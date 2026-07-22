class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        i = len(digits) - 1
        while i >= 0:
            if digits[i] != 9:
                digits[i] += 1
                return digits
            else:
                digits[i] = 0
                i -= 1
            
            if digits[0] == 0:
                digits[0] = 1
                digits.append(0)
                for i in range(1, len(digits)):
                    digits[i] = 0
                return digits