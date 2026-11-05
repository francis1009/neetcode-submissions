class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dicti = {}
        for i in range(len(strs)):
            s_alpha = [0]*26
            stri = strs[i]
            for j in range(len(stri)):
                s_alpha[ord(stri[j])-ord('a')] += 1
            tup = tuple(s_alpha)
            if tup not in dicti:
                dicti[tup] = [strs[i]]
            else:
                dicti[tup].append(strs[i])
        ans = []
        for values in dicti.values():
            ans.append(values)
        return ans
