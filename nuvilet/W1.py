# animals = ['dog', 'cat', 'bat', 'cock', 'cow', 'pig', 'fox', 'ant', 'bird', 'lion', 'wolf', 'dear', 'bear', 'frog', 'hen', 'mole', 'duck', 'goat']
    
    
# st = 'dogdogdogdogdog'
# lst = []
    
# for i in range(len(animals)):
#     for j in range(len(animals[i])):
#         if not animals[i][j] in st:
#             break
#         elif j == len(animals[i])-1:
#             lst.append(animals[i])
            
# print(lst)




# domino_num = [[0,0],[0,1],[0,2],[0,3],[0,4],[0,5],[0,6],[1,1],[1,2],[1,3],[1,4],[1,5],[1,6],[2,2],[2,3],[2,4],[2,5],
#               [2,6],[3,3],[3,4],[3,5],[3,6],[4,4],[4,5],[4,6],[5,5],[5,6],[6,6]]

# input_num = '[[0,1], [0,2], [0,3]]'#input('num = ')
# lst = eval(input_num)
# lst2 = []

# for i in domino_num:
#     if i not in lst:
#         lst2.append(i)
        
        
# print(lst2)


# lst1 = [1, 0, 2, 3, 0, 4, 5, 0]
# lst2 = []

# for i in lst1:
#     if i == 0:
#         lst2.append(0)
#         lst2.append(0)
#     else:
#         lst2.append(i)
        
# print(lst2)




# trian1 = [[0,0], [1,2], [2,0]]
# trian2 = [[1,0], [1,2], [2,0]]
# bool1 = False
# bool2 = False

# if trian1[0][0] == trian1[1][0] or trian1[0][0] == trian1[2][0] or trian1[1][0] == trian1[2][0]:
#     bool1 = True
# else:
#     bool1 = False
    
# if trian2[0][0] == trian2[1][0] or trian2[0][0] == trian2[2][0] or trian2[1][0] == trian2[2][0]:
#     bool2 = True
# else:
#     bool2 = False
    
# if bool1 == bool2:
#     print('True')
# elif bool1 != bool2:
#     print("False")


# data = ''
# with open('c.txt', 'r') as file:
#     data = file.read()
# data = data.split('\n')
# data[4] = "    a++;"
# data[6] = "    b++;"
# data = "\n".join(data)


# with open("c.txt", 'w') as file:
#     file.write(data)
    



  

