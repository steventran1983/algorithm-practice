# 1 2 3 
# 4 5 6 
# 7 8 9

# 1. Transpose matrix

# 1 4 7
# 2 5 8
# 3 6 9

# 2. swap first and last element in row

# 7 4 1 
# 8 5 2
# 9 6 3

matrix = [[1,2,3],[4,5,6],[7,8,9]]

def transpose(matrix):
  n = len(matrix)
  for i in range(0,n):
    for j in range (i,n):
      tmp = matrix[i][j]
      matrix[i][j] = matrix[j][i]
      matrix[j][i] = tmp
  
def rotate(matrix):
  n = len(matrix)
  for i in range(0,n):
    for j in range(0,n//2):
      tmp = matrix[i][j]
      matrix[i][j] = matrix[i][n - j -1]
      matrix[i][n -j -1] = tmp
  
  


if __name__ == "__main__":
  transpose(matrix)
  print(matrix)
  rotate(matrix)
  print(matrix)