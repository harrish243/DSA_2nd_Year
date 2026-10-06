class Solution(object):
    def largestAltitude(self,gain):
        current = 0
        highest = 0

        for i in gain:
            current = current + i
            highest = max(highest, gain)

        return highest