class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        carry = 1
        for i in reversed(range(len(digits))):
            if digits[i] + 1 == 10:
                digits[i] = 0
            else:
                digits[i] += 1
                carry = 0
                break
        if carry:
            digits.insert(0, 1)
        return digits
