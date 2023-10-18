# class Solution:
#     def reverseWords(self, s: str) -> str:
#         s = s.split()
#         for i in range(len(s)):
#             s[i] = s[i][::-1]
            
#         s = ' '.join(s)
#         return s
    
# s = "Let's take LeetCode contest"

# sol = Solution()
# print(sol.reverseWords(s))




# class Solution:
#     def areNumbersAscending(self, s: str) -> bool:
#         prev_num = -1
#         num = 0
#         bll = None
#         s = s.split()
#         for i in s:
#             if i.isdigit():
#                 num = int(i)
#                 if num > prev_num:
#                     bll = True
#                 elif num <= prev_num:
#                     bll = False
#                     break
#             prev_num = num 
        
#         return bll
    
    
    
# s = "sunset is at 7 51 pm overnight lows will be in the low 50 and 60 s"
# sol = Solution()
# print(sol.areNumbersAscending(s))







# Input: s = "ab-cd"
# Output: "dc-ba"

class Solution:
    def reverseOnlyLetters(self, s: str) -> str:
        # s = s.split('-')
        
        s = s[::-1]
        return s
    
sol = Solution()
s = "a-bC-dEf-ghIj"

print(sol.reverseOnlyLetters(s))
    
    

        
        
        
        
        
        
        
        
        
        
        
        
        