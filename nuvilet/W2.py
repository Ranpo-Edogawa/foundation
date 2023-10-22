from math import sqrt
class Solution:
    
    def isPrime(self, n: int) -> bool:
        if n <= 1:
           return False 
        if n % 2 == 0:
            if n == 2:
                return True
            else:
                return False
        stop = int(sqrt(n)+1)
        for i in range(3, stop, 2):
           if n % i == 0:
               return False
       
        return True

    
    
    def diagonalPrime(self, nums: list[list[int]]) -> int:
        lst = []
        for i in range(len(nums)):
            for j in range(len(nums[i])):
                if j == i or j == len(nums[i]) - i - 1:
                    if self.isPrime(nums[i][j]):
                        lst.append(nums[i][j])
        nums.clear()
        return max(lst) if lst else 0
    
    
    
nums = [[1,2,3],[5,6,7],[9,10,11]]

print(Solution().diagonalPrime(nums))