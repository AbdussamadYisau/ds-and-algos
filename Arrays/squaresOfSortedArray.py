class Solution:
    def sortedSquares(self, A: List[int]) -> List[int]:
        solArray = []
        
        for num in A:
            solArray.append(num**2)
        solArray.sort()
        
        return solArray
        