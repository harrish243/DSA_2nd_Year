class Solution(object):
    def largestAltitude(self, gain):
        maximum=0
        ap=0
        for i in gain:
            ap +=i
            maximum= max(maximum,ap)
        return maximum