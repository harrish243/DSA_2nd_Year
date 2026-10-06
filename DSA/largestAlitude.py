class Solution:
    def largestAltitude(self, gain: list[int]) -> int:
        hig_alt = [0]
        sum = 0
        for i in range(len(gain)):
            sum += gain[i]
            hig_alt.append(sum)

        return max(hig_alt)