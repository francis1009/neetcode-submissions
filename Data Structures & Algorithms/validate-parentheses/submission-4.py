class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for c in s:
            if c == '(' or c == '[' or c == '{':
                stack.append(c)
                continue
            if len(stack) == 0:
                return False
            op = stack.pop()
            if op == '(' and c != ')':
                return False
            if op == '[' and c != ']':
                return False
            if op == '{' and c != '}':
                return False
        if len(stack) != 0:
            return False
        return True