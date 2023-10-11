class Solution:
    def validMountainArray(self, arr: list[int]) -> bool:
        count = 0
        count1 = 0
        for i in range(len(arr)-1):
            if arr[i] < arr[i+1]:
                count += 1
            elif arr[i] == arr[i+1]:
                return False
            else:
                count -= 1
            if count1 != count:
                return False
            
            count1 = count
            
            
            
            
sol = Solution()
print(sol.validMountainArray([0,3,2,1]))
           
        