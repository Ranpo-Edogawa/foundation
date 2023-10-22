# class Solution:
    
#     def maximumWealth(self, accounts):
#         max_wealth = 0
#         for customer in accounts:
#             if sum(customer) > max_wealth:
#                 max_wealth = sum(customer)
#         return max_wealth



# sol = Solution()

# print(sol.maximumWealth([[1,2,3],[3,2,1]]))


# class Solution:
#     def diagonalSum(self, mat: list[list[int]]) -> int:
#         sum = 0
#         for i in range(len(mat)):
#             for j in range(len(mat[i])):
#                 if j == i:
#                     sum += mat[i][j]
#                 if len(mat) - i == j + 1:
#                     sum += mat[i][j]
                
#         if len(mat) % 2 == 1:
#             sum -= mat[len(mat) // 2][len(mat) // 2]
                    
#         return sum
    
    
    
    
# sol = Solution()
# print(sol.diagonalSum([[1,2,3],[4,5,6],[7,8,9]]))



# Element at grid[i][j] moves to grid[i][j + 1].
# Element at grid[i][n - 1] moves to grid[i + 1][0].
# Element at grid[m - 1][n - 1] moves to grid[0][0].




# class Solution:
#     def shiftGrid(self, grid: list[list[int]], k: int) -> list[list[int]]:
#         m = len(grid)
#         n = len(grid[0])
#         k = k % (m * n) # reduce k to the minimum number of shifts
#         result = [[0] * n for _ in range(m)] # create a new grid with the same size
#         for i in range(m):
#             for j in range(n):
#                 new_i = (i + (j + k) // n) % m # calculate the new row index
#                 new_j = (j + k) % n # calculate the new column index
#                 result[new_i][new_j] = grid[i][j] # assign the value from the original grid to the new grid
#         return result

                    
                

# sol = Solution()
# print(sol.shiftGrid([[1,2,3],[4,5,6],[7,8,9]], 2))  






#     class Solution:
#         def matrixReshape(self, mat: list[list[int]], r: int, c: int) -> list[list[int]]:
#             if len(mat) * len(mat[0]) != r * c:
#                 return mat
            
#             lst = []
#             for x in range(r):
#                 lst.append([])
#                 for i in range(len(mat)):
#                     for j in range(len(mat[i])):
#                         lst[x].append(mat[i][j])
                        
#             return lst
    
    
    
# sol = Solution()
# print(sol.matrixReshape([[1,2],[3,4]], 1, 4))



# def reshape_matrix(mat, r, c):
#     m, n = len(mat), len(mat[0])
#     if m * n != r * c:
#         return mat
#     result = [[0] * c for _ in range(r)]
#     for i in range(m * n):
#         result[i // c][i % c] = mat[i // n][i % n]
#     return result



# print(reshape_matrix([[1,2],[3,4]], 1, 4))




class Solution:
    def isValidSudoku(self, board: list[list[str]]) -> bool:
        for i in range(9):
            for j in range(9):
                if board[i][j] != '.':
                    for x in range(9):
                        for y in range(9):
                            if board[i][j] == board[x][j]:
                                return False
                            if board[i][j] == board[i][y]:
                                return False    
        return True
    
    
    
    
    
    
    
board = [["5","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]

sol =Solution()


print(sol.isValidSudoku(board))

