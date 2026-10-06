class Solution:
    def largestAltitude(self, gain: list[int]) -> int:
        max = 0
        n = 0
        for i in gain:
            n += i
            if(n > max):
                max = n
        return max
            