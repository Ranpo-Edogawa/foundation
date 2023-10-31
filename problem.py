

# def fridey(data, data2):
#     data = data.split('.')
#     day = int(data[0])
#     month = int(data[1])
#     year = int(data[2])
#     data2 = data2.split('.')
#     day2 = int(data2[0])
#     month2 = int(data2[1])
#     year2 = int(data2[2])
#     if month == month2:
#         if day < day2 and day2 - day > 7 or day > day2 and day - day2 > 7:
#             if month % 2 == 0:
#                 month -= 3
#             elif month % 2 == 1:
#                 month -= 3
#                 day -= 1
#                 if day < 0:
#                     day = abs(day)
#                     month -= 1
#                 if month < 0:
#                     month = abs(month)
#                     year-=1
#         if day < day2 and not day2 - day > 7 and day > day2 and not day - day2 > 7:
#             while True:
#                 day -= 7
#                 if day < day2-7:
#                     break
#             if month % 2 == 0:
#                 month -= 3
#             elif month % 2 == 1:
#                 month -= 3
#                 day -= 1
#                 if day < 0:
#                     day = abs(day)
#                     month -= 1
#                 if month < 0:
#                     month = abs(month)
#                     year-=1
#     return f"{day}.{month}.{year}"
    
        



# data = '28.10.2023'
# data2 = '26.10.2023'    

# print(fridey(data, data2))


#Ex: Completed
# with open('text.txt', 'r') as file:
#     data = file.read()


# lst1 = ['a', 'q', 'w', 'e', 'r', 's', 'd', 'f', 'z', 'c', 'v', 't', 'g', 'b', '1', '2', '3', '4', '5', '!', '@', '#', '$', '%']
# lst2 = ['y', 'u', 'h', 'j', 'n', 'm', 'i', 'o', 'p', 'l', '6', '7', '8', '9', '0', '^', '&', '*', '(', ')', '-', '_', '=', '+']

# ung = 0
# chap = 0
# for i in data:
#     i = i.lower()
#     if i in lst1:
#         chap += 1
#     if i in lst2:
#         ung += 1
# print(f"O`ng qo`lda {ung} ta, Chap qo`lda {chap} ta ")



# #Ex:
# class Fraction:
#     def __init__(self, Numerator, Denominator) -> None:
#         self.num = Numerator
#         self.den = Denominator
    

#     def minus(self, fr1, fr2):
#         ''' a - b -> 
#         '''
#         if fr1.den == fr2.den:
            
#             fr1.num -= fr2.num
#         else:
#             fr1.num *= fr2.den
#             fr2.num *= fr1.den
#             fr1.den = fr1.den * fr2.den
#             fr2.den = fr1.den
#             fr1.num -= fr2.num
        
#         return f'{fr1.num}/{fr1.den}'
#     def plus(self, fr1, fr2):
#         if fr1.den == fr2.den:
#             fr1.num += fr2.num
#             if fr1.num >= fr1.den:
#                 return f"{fr1.num // fr2.den}|{fr1.num % fr1.den}/{fr1.den}"
#         else:
#             fr1.num *= fr2.den
#             fr2.num *= fr1.den
#             fr1.den = fr1.den * fr2.den
#             fr2.den = fr1.den
#             fr1.num += fr2.num
#             if fr1.num >= fr1.den:
#                 return f"{fr1.num // fr2.den}|{fr1.num % fr1.den}/{fr1.den}"
#         return f'{fr1.num}/{fr1.den}'
        
        
        
#     def multiple(self, fr1, fr2):
#         fr1.num *= fr2.num
#         fr1.den *= fr2.den
#         return f'{fr1.num}/{fr1.den}'
        
#     def buluv(self, fr1, fr2):
#         fr1.num *= fr2.den
#         fr1.den *= fr2.num
#         return f'{fr1.num}/{fr1.den}'
        
        
        

# fr1 = Fraction(int(input('fr1.num: ')), int(input('fr1.den: ')))
# fr2 = Fraction(int(input('fr2.num: ')), int(input('fr2.den: ')))
# print(fr1.plus(fr1, fr2))

# n = int(input('n = '))
# k = int(input('k = '))
# m = int(input('m = '))
# lst = []
# for i in range(m):
#     lst.append(input())
# lst2 = []
# lst = list(map(lambda x: x.split(), lst))
# lst2.append(lst[0])
# lst3 = [1]
# for i in range(1, n+1):
#     for j in lst:
#         if j not in lst2:
#             if len(lst2) <= 2:
#                 lst2.append(j)
#                 lst3.append(1)
            
#             if len(lst2) == 2:
#                 lst3.append(0)
                
#             if int(j[1]) == i:
#                 for x in range(len(lst2)):
#                     if lst2[x] == j:
#                         lst2.pop(x)
        
        
    

# print(lst3)
    
            
         
# def integer(num):
#     for i in range(len(num)):
#         num[i] = int(num[i])         
#     return num
# s = int(input('s = '))

# n = int(input('n = '))

# p = input('p = ')
# p = p.split()
# p = integer(p)

# m = int(input('m = '))

# q = input('q = ')
# q = q.split()
# q = integer(q)

# for i in p:
#     if s > 0:
#         print(f'+{i}')
#         s-=i
#     if s < 0:
#         break
# if s > 0:
#     print('impossible')
# else:
#     for i in q:
#         if s < 0:
#             print(f'{s}')
#             s += i
#     if s < 0:
#         print('impossible')
    

        
      
            
        
        