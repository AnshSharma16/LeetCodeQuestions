class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        allNodes=set(range(n))
        destNodes=set(dest for _, dest in edges)
        srcNodes=allNodes-destNodes
        return list(srcNodes)