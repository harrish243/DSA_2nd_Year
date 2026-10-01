class Solution:
    def maximumWealth(self, accounts: list[list[int]]) -> int:
        max_res = 0
        for i in accounts:
            wealth = 0
            for j in i:
                wealth += j
                if wealth > max_res:
                    max_res = wealth
        return max_res