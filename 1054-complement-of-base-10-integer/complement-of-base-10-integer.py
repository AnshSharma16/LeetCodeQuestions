class Solution(object):
    def bitwiseComplement(self, n):
        """
        :type n: int
        :rtype: int
        """
        b=bin(n)
        binary=b[2:]
        comp=''.join('1' if ch=='0' else '0' for ch in binary )
        return int(comp,2)


        