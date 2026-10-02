class Solution:
    def maximumWealth(self, accounts: list[list[int]]) -> int:
        max_wealth=0
        for customer in accounts:
            wealth=sum(customer)
            max_wealth=max(max_wealth,wealth)
        return max_wealth
accounts=[[1,2,3],[3,2,1]]
print(Solution().maximumWealth(accounts))