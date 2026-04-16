class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        longest = 0
        if not s:
            return 0
        
        # charset = set()

        # l = 0
        # for r in range(len(s)):
        #     while s[r] in charset:
        #         charset.remove(s[l])
        #         l += 1
        #     charset.add(s[r])
        #     longest = max(longest, r - l+ 1)
        # return longest


        mp = {}

        l = 0
        for r in range(len(s)):
            if s[r] in mp:
                l = max(1 + mp[s[r]], l)
            
            mp[s[r]] = r
            longest = max(longest, r - l+ 1)
        return longest



