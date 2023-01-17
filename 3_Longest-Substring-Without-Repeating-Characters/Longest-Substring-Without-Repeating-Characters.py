class Solution(object):
    def lengthOfLongestSubstring(self, s):
        dictionary = {}

        start = 0
        longest = 0

        for index in range(0, len(s)):

            if s[index] in dictionary:
                if dictionary[s[index]] + 1 > start:
                    start = dictionary[s[index]] + 1

            dictionary[s[index]] = index
            if index - start + 1 > longest:
                longest = index - start + 1

        return longest
