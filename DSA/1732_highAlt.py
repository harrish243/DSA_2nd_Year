class Solution(object):
    def largestAltitude(self, gain):
        current=0
        high=0
        for i in gain:
            current=current+ i
            if current>high:
                high=current
        return high