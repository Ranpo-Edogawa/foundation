class Solution:
    def addTwoNumbers(self, l1, l2):
        l1 = ''.join(map(str, l1))
        l2 = ''.join(map(str, l2))
        l3 = int(str(l1)[::-1]) + int(str(l2)[::-1])
        l3 = int(str(l3)[::-1])
        return l3




l1 = [2,4,3] 
l2 = [5,6,4]

print(Solution().addTwoNumbers(l1,l2)) 



class Solution:
    def removeElement(self, nums: list[int], val: int) -> int:
        while val in nums:
            nums.remove(val)
            nums.append('_')
            
        k = nums.index('_')
        return k, nums
    
        
raqamlar = [0,1,2,2,3,0,4,2]
val = 2

print(Solution().removeElement(raqamlar, val))







class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if needle not in haystack:
            return -1
        else:
            return haystack.index(needle)
        
        
        
    
        
# hayctack = "sadbutsad"
# needle = "sad"

# Solution().strStr(hayctack, needle)






























