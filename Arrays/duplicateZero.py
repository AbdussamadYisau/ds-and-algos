class Solution:
    def duplicateZeros(self, arr):
        """
        Do not return anything, modify arr in-place instead.
        """
        newArr = []

        n = len(arr)
        
        for i in range(n-1):
            if arr[i] != 0:
                newArr[i] = arr[i]
            else: 
                newArr[i] = arr[i]
                newArr[i+1] = 0

                i += 1

                
        print(arr)

t = Solution()
print(t.duplicateZeros([1,0,2,3,0,4,5,0]))