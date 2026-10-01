" question 9 https://leetcode.com/problems/palindrome-number/"
class Solution:
    def isPalindrome(self, x: int) -> bool:
        a = x
        b = 0
        if  x < 0:
            return False
        while x > 0:
            d = x % 10
            b = b*10 + d
            x = x // 10
        return a == b
        
         