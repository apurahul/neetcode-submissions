class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        # sorted_strs = {}
        

        # for string in strs:
        #     sorted_str = ''.join(sorted(string))
        #     if sorted_str in sorted_strs:
        #         sorted_strs[sorted_str].append(string)
        #     else:
        #         sorted_strs[sorted_str] = [string]
        
        # return list(sorted_strs.values())


        #the above is O(n * mlog m), space - O(n* m)

    #optimal approach is to get thre frequency of the characters of eacch string, make that tuple key and check and keep adding

        res = defaultdict(list) 

        

        for s in strs:

            count = [0]*26

            for c in s:
                count[ord(c) - ord('a')] += 1
            res[tuple(count)].append(s)

        return list(res.values())

        
