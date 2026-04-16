class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        if len(s1) > len(s2):
            return False
        
        # count1= {}
        # for c in s1:
        #     count1[c] = 1 + count1.get(c, 0)
        
        # need = len(count1)

        # for  i in range(len(s2)):
        #     count2 = {}
        #     curr = 0

        #     for j in range(i, len(s2)):
        #         count2[s2[j]] = 1 + count2.get(s2[j], 0)
        #         if count1.get(s2[j], 0) < count2[s2[j]]:
        #             break
                
        #         if count1.get(s2[j], 0) == count2[s2[j]]:
        #             curr += 1
                
        #         if curr == need:
        #             return True
        # return False

        # l = 0
        # count2 = {}

        # for r in range(len(s2)):

        #     count2[s2[r]] = 1 + count2.get(s2[r], 0)

        #     if (r - l + 1) > len(s1):
        #         count2[s2[l]] -= 1

        #         if count2[s2[l]] == 0:
        #             del count2[s2[l]]

        #         l += 1

        #     if count1 == count2:
        #         return True

        # return False


        count1, count2 = [0]*26, [0]*26

        for i in range(len(s1)):
            count1[ord(s1[i]) - ord('a')] += 1
            count2[ord(s2[i]) - ord('a')] += 1

        matches = 0

        for i in range(26):
            if count1[i] == count2[i]:
                matches += 1
            else:
                0
        l = 0
        for r in range(len(s1), len(s2)):
            if matches == 26:
                return True
            
            index = ord(s2[r]) - ord('a')
            count2[index] += 1

            if count1[index] == count2[index]:
                matches += 1
            elif count1[index] + 1 == count2[index]:
                matches -= 1


            index = ord(s2[l]) - ord('a')
            count2[index] -= 1

            if count1[index] == count2[index]:
                matches += 1
            elif count1[index] - 1 == count2[index]:
                matches -= 1

            l += 1
        return matches == 26
            


                
        