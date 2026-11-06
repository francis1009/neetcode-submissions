class Solution:
    def isPalindrome(self, s: str) -> bool:
        s1 = ""
        for c in s:
            if c.isalnum():
                s1 += c.lower()
        p1, p2 = 0, len(s1)-1
        while p1 < p2:
            while not s1[p1].isalnum():
                p1 += 1
                if p1 == len(s1):
                    return False
            while not s1[p2].isalnum():
                p2 -= 1
                if p2 == -1:
                    return False
            if s1[p1] != s1[p2]:
                return False
            p1 += 1
            p2 -= 1
        return True