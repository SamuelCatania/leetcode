class Solution:
    def longestPalindrome(self, s: str) -> int:
        dict = {}
        length = 0
        input_length = 0

        for letter in s:
            dict[letter] = dict[letter] + 1 if letter in dict else 1

            if dict[letter] % 2 == 0:
                length += 2

            input_length += 1

        return length + 1 if input_length > length else length
