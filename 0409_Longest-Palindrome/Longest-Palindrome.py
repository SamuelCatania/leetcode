class Solution:
    def longestPalindrome(self, s: str) -> int:
        dict = {}
        length = 0

        for letter in s:
            dict[letter] = dict[letter] + 1 if letter in dict else 1

            if dict[letter] % 2 == 0:
                length += 2

        return length + 1 if len(s) > length else length
