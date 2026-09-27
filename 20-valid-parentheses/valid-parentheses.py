class Solution:
    def isValid(self, s: str) -> bool:
        dc={
            ']':'[',
            '}':'{',
            ')':'('
        }
        stack=[]

        for b in s:
            if b in '({[':
                stack.append(b)

            else:
                if not stack or  stack.pop()!=dc[b]:
                    return False
        return not stack