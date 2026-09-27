class Solution:
    def isPalindrome(self, s: str) -> bool:
        st=''
        for ch in s:
            if ch not in string.punctuation:
                st+=ch
        res=st.replace(" ","").lower()
        if res == res[::-1]:
            return True
        else:
            return False