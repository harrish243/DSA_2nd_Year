'''
leetcode 9
https://leetcode.com/problems/palindrome-number/
'''

class Solution(object):
    def isPalindrome(self, x):
        original = x
        reverse = 0
        while x > 0:
            remainder = x%10
            reverse = (reverse *10) + remainder
            x//=10
    
        return reverse == original