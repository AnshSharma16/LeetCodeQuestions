class Solution:
    def lengthOfLastWord(self, s: str) -> int:

        string=s.strip()
        arr=string.split()
        
        return (len(arr[len(arr)-1]))