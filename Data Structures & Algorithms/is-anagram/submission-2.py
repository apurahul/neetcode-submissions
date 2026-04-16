class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        from collections import Counter

        dict1 = dict(Counter(s))
        dict2 = dict(Counter(t))

        if dict1 == dict2:
            return True
        return False


        