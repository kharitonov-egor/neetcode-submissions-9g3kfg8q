class Solution:
    def isValid(self, s: str) -> bool:


        stack = []

        for par in s:
            if par == "(" or par == "{" or par == "[":
                stack.append(par)
            else:
                if len(stack) == 0: return False
                top = stack[-1]
                stack.pop()
                if top == "(" and par != ")": return False
                if top == "{" and par != "}": return False
                if top == "[" and par != "]": return False

        return len(stack) == 0
        