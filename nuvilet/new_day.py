# class Number:
#     def __init__(self) -> None:
#         self.dct = ['(', ')', '-', '-', '-']
#         pass
    
    
#     def check_true_phone_number(self, phone_number):
#         if len(phone_number) != 18:
#             print("Your phone number is not correct", len(phone_number))
#             return False
#         for i in self.dct:
#             if i not in phone_number:
#                 print("Your phone number is not correct", i)
#                 return False
#         return True 
    
    
# mobile_phone = Number()
# mobile_phone_number = input("Enter your mobile phone number: ")
# print(mobile_phone.check_true_phone_number(mobile_phone_number))



# class Birthday:
#     def __init__(self) -> None:
#         pass
    

#     def check_birthday(self, birthday, name):
#         if birthday % 2 == 0:
#             text = f'{birthday} Happy birthday {name}! {birthday}'
#             self.print_birthday_1(text)
#         else:
#             text = f'{birthday} Happy birthday {name}! {birthday}'
#             self.print_birthday_2(text)
        
#     def print_birthday_1(self, tabrik):
        
#         print('#'*(len(tabrik)+4))
#         print('#', tabrik, '#')
#         print('#'*(len(tabrik)+4))
        
        
#     def print_birthday_2(self, tabrik):
        
#         print('*'*(len(tabrik)+4))
#         print('*', tabrik, '*')
#         print('*'*(len(tabrik)+4))
        
        
        
# person = Birthday()
# person.check_birthday(24, 'Levi')



