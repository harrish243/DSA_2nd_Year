class Solution:
    def isPalindrome(self, x):
        if x < 0:
            return False

        reverse = 0
        num = x

        while num != 0:
            reverse = reverse * 10 + num % 10
            num = num // 10

        return reverse == x