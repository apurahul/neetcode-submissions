class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

       # return sorted(s) == sorted(t)

       #using hash maps

       #create 2 dictionaries and then compare them

        # countS = {}
        # countT = {}

        # for i in range(len(s)):
        #     countS[s[i]]  = 1 + countS.get(s[i], 0)
        #     countT[t[i]]  = 1 + countT.get(t[i], 0)
        
        # return countS == countT


        #simplest way - time O(n + m), space is o(1)


        count = [0] * 26

        for i in range(len(s)):
            count[ord(s[i]) - ord('a')] += 1
            count[ord(t[i]) - ord('a')] -= 1

        for val in count:
            if val != 0:
                return False
            
        return True








        