class Solution:
    def isPalindrome(self, s: str) -> bool:
        st=''
        for ch in s:
            if ch not in string.punctuation:
                st+=ch
        res=st.replace(" ","").lower()
        
        left=0
        right=len(res)-1

        while left<right:
            if res[left]!=res[right]:
                return False

            right-=1
            left+=1
        
        return True