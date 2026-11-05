class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ans = defaultdict(list)
        for s in strs:
            s_alpha = [0]*26
            for c in s:
                s_alpha[ord(c)-ord('a')] += 1
            ans[tuple(s_alpha)].append(s)
        return list(ans.values())
