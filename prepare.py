# ex: 1
# def to_Camelcase(text):
#     text = text.split('_')
#     for i in range(1, len(text)):
#         text[i] = text[i].capitalize()
#     text = ''.join(text)
    
#     return text


# def to_snakecase(text):
#     for i in range(len(text)):
#         if text[i].isupper():
#             text = text.replace(text[i], '_' + text[i][0].lower())
    
#     return text

# text1 = 'hello_codechick'
# text2 = 'helloCodechick'

# print(to_Camelcase(text1))
# print(to_snakecase(text2))

# ex: 2
# def matrix(num) -> list[list]:
#     mat = []
#     for i in range (num):
#         row = []
#         for j in range (num):
#             if i == j or i + j == num - 1:
#                 row.append(1)
#             else:
#                 row.append(0)
#         mat.append (row)
#     return mat
    

# n = int(input('n = '))

# lst = matrix(n)
# for i in lst:
#     for j in i:
#         print(j, end = ' ')
#     print()



# ex: 3
# def like(lst):
#     if len(lst) == 0:
#         return 'no one likes this'
#     elif len(lst) == 1:
#         return f'{lst[0]} likes this'
#     elif len(lst) == 2:
#         return f'{lst[0]} and {lst[1]} like this'
#     elif len(lst) > 2:
#         for i in range(len(lst) - 2):
#             lst[i] = lst[i] + ', '
#         lst[-2] = lst[-2] + ' and '
#         lst[-1] = lst[-1] + ' like this'
#         return ''.join(lst)
    
    
# text = ['Anthon', 'Mark']

# print(like(text))




#ex: 4
# def caeser_cipher(text, shift):
  
#     text = list(text)
    
#     for i in range(len(text)):
#         text[i] = chr(ord(text[i]) + shift)
        
#     return ''.join(text)


# text = 'hello'
# shift = 5
# print(caeser_cipher(text, shift))






#ex: 5 ------- qayta ko`rish
# def adfgx_encrypt(word, square, key):
#     # Polibiy kvadratini yaratish
#     alphabet = "ABCDEFGHIKLMNOPQRSTUVWXYZ" # J harfini olib tashlaymiz
#     square = square.upper() # Kvadratni katta harflarga o'tkazamiz
#     key = key.upper() # Kalit so'zni katta harflarga o'tkazamiz
#     word = word.upper() # So'zni katta harflarga o'tkazamiz
#     word = word.replace("J", "I") # J harfini I bilan almashtiramiz
#     matrix = [] # Kvadratni saqlash uchun bo'sh ro'yxat
#     for letter in square: # Kvadratdagi harflarni birinchi navbatda qo'shamiz
#         if letter in alphabet and letter not in matrix:
#             matrix.append(letter)
#     for letter in alphabet: # Qolgan harflarni tartib bilan qo'shamiz
#         if letter not in matrix:
#             matrix.append(letter)
    
#     # Matnni kvadratga moslashtirish
#     adfgx = "ADFGX" # Indeks sifatida ishlatiladigan harflar
#     cipher = "" # Shifrlangan matnni saqlash uchun bo'sh satr
#     for letter in word: # Har bir harf uchun
#         index = matrix.index(letter) # Kvadratdagi indeksini topamiz
#         row = index // 5 # Satr indeksini hisoblaymiz
#         col = index % 5 # Ustun indeksini hisoblaymiz
#         cipher += adfgx[row] + adfgx[col] # Shifrlangan matnga qo'shamiz
    
#     # Matnni tartiblashtirish
#     sorted_key = sorted(key) # Kalit so'zni alifbo tartibida saralaymiz
#     table = [] # Tartiblash uchun jadval yaratamiz
#     for i in range(len(key)): # Har bir ustun uchun
#         column = [] # Ustunni saqlash uchun bo'sh ro'yxat
#         column.append(key[i]) # Ustunning boshiga kalit so'zning harfini qo'shamiz
#         for j in range(i, len(cipher), len(key)): # Shifrlangan matndan ustunning elementlarini olamiz
#             column.append(cipher[j])
#         table.append(column) # Jadvalga ustunni qo'shamiz
    
#     # Matnni yuborish
#     final_cipher = "" # Natijaviy shifrlangan matnni saqlash uchun bo'sh satr
#     for letter in sorted_key: # Kalit so'zning saralanmagan harflari bo'yicha ustunlarni olamiz
#         index = key.index(letter) # Ustunning indeksini topamiz
#         for i in range(1, len(table[index])): # Ustunning elementlarini natijaviy shifrlangan matnga qo'shamiz
#             final_cipher += table[index][i]
    
#     return final_cipher # Natijaviy shifrlangan matnni qaytaramiz

# # Funksiyani sinab ko'ramiz

# word = "hello" # Shifrlash kerak bo'lgan so'z
# square = "bing" # Kvadrat uchun kalit so'z
# key = "code" # Tartiblash uchun kalit so'z

# encrypted_word = adfgx_encrypt(word, square, key) # Funksiyani chaqiramiz

# print(encrypted_word) # Natijani chop etamiz






# class Book:
    
#     def __init__(self, name, count_pages, price) -> None:
#         self.name = name
#         self.count_pages = count_pages
#         self.price = price


#     def page_price(self) -> float:
#         return self.count_pages / self.price


#     def name_equal_price(self, books):
#         self.programm_book_names = ['Python', 'Java', 'PHP', 'C#', 'C++', 'JavaScript']
#         for i in range(len(books)):
#             if books[i].name in self.programm_book_names:
#                 books[i].price = books[i].price * 2
#         return books
    
#     def __str__(self) -> str:
#         return f'{self.name} {self.count_pages} {self.price}'


# b1 = Book('Python', 200, 150)
# b2 = Book('C++', 300, 100)
# b3 = Book('Graf Monte Kristo', 400, 200)
# b4 = Book('C#', 500, 250)
# b5 = Book('Poirot', 600, 300)

# books = [b1, b2, b3, b4, b5]
# print(*b1.name_equal_price(books))

# print(*books)





# ex: 6


# M = int(input('M = '))
# N = int(input('N = '))
# info = input("EXAMPLE: Sanjar 1 5 Baxrom 2 5 Kamola 1 2\n")
# # info = 'Sanjar 1 5 Baxrom 3 5 Kamola 1 2'#input('info = ')
# info = info.split()
# lst = []

# for i in range(0, len(info), 3):
#     lst.append([info[i+1], info[i+2]])

# lst2 = []
# counter = 0
# for i in range(1, M+1):
#     for j in range(len(lst)):
#         if i == int(lst[j][0]):
#             counter += 1
#         if int(lst[j][1]) == i:
#             counter -= 1
#     lst2.append(counter)

# for i in range(len(lst2)):
#     if lst2[i] == max(lst2):
#         print(f"{i+1} - {i + 2}")



# def to_shrift(alpha, text):
#     key = 'ADFGX'
#     matrix = list()
    
#     matrix = [key[i] + key[j] for i in range(5) for j in range(5)]

#     matrix = tuple(matrix)
#     dct = dict(zip(alpha, matrix))
#     text = list(text)
#     for i in range(len(text)):
#         text[i] = dct[text[i]]
#     return ''.join(text)
        
    
# alpha = 'bchigklnmoqprstuvwxyzadef'
# text = 'helloworld'
# text = to_shrift(alpha, text)
# print(text)

    






