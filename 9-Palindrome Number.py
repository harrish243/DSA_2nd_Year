class Solution:
    def isPalindrome(self, x: int) -> bool:
        original=x
        result=0
        while x>0:
            ldigit=x%10
            result=(result*10)+ldigit
            x=x//10
        return original==result