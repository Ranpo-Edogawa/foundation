# dct = {0: 'nol', 1: 'bir', 2: 'ikki', 3: 'uch', 4: 'tort', 5: 'besh', 6: 'olti', 7: 'yetti', 8: 'sakkiz', 9: 'toqqiz', 10: 'on', 
#        20: 'yigirma', 30: 'o\'ttiz', 40: 'qirq', 50: 'ellik', 60: 'oltmish', 70: 'yetmish', 80: 'sakson', 90: 'toqson', 100: 'yuz',
#        1000: 'ming', 2000: 'ming', 3000: 'ming', 4000: 'ming', 5000: 'ming', 6000: 'ming', 7000: 'ming', 8000: 'ming', 9000: 'ming', 10000: 'ming'
#        }

# num = int(input('num = '))

# lst = []
# n = len(str(num)) - 1
# lst.append(num % 10)
# num = num // 10    

# for i in range(1, len(str(num))):
#     lst.append((num % 10) * (10 ** i))
#     num = num // 10
# lst.append(int(str(num)[0]) * (10 ** n))


# lst.reverse()
# for i in lst:
#     print(dct[i], end = ' ')   
import num2word


num = int(input('num = '))

n = num.num2word.digitToWord()
print(n)
    
 