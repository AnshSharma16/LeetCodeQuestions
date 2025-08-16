class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        
        dict={"2": "abc", "3": "def", "4":"ghi", "5": "jkl", "6":"mno","7":"pqrs","8":"tuv","9":"wxyz"}
        res=['']

        if not digits or digits=='1':
            return []

        for i in digits:
            res=[j+k for j in res for k in dict[i]]
        return res


        
