class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        pre = strs[0]
        for str in strs[1:]:
            while not str.startswith(pre):
                pre = pre[:-1]
                if pre == "":
                    return ""
        return pre

'''14. Longest Common Prefix
Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".'''

