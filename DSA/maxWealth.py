class Solution:
    def maximumWealth(self, accounts: list[list[int]]) -> int:
        sum=0
        for i in range(len(accounts)):
            total=0
            for j in range(len(accounts[i])):
                total=total+accounts[i][j]
            if total>sum:
                sum=total
        return sum
            