#Longest common prefix
class Solution(object):
    def longestCommonPrefix(self, strs):
        prefix = strs[0]

        for word in strs[1:]:
            while not word.startswith(prefix):
                prefix = prefix[:-1]

                if prefix == "":
                    return ""

        return prefix
#Write a function to find the longest common prefix string amongst an array of strings.

#If there is no common prefix, return an empty string "".
        