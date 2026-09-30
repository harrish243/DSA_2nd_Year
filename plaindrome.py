" question 9 https://leetcode.com/problems/palindrome-number/"
class Solution:
    def isPalindrome(self, x: int) -> bool:
        y = str(x)
        z = y[::-1]
        if z == y:
            return True
        else:
            return False
        