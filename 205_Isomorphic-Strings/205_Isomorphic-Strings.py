class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        dict_st = {}
        dict_ts = {}

        for index, letter in enumerate(s):
            if letter in dict_st and dict_st[letter] != t[index] or t[index] in dict_ts and dict_ts[t[index]] != letter:
                return False
            else:
                dict_st[letter] = t[index]
                dict_ts[t[index]] = letter
        
        return True
