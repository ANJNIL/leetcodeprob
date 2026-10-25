class Solution(object):
    def spiralOrder(self, matrix):
        result = []
        left =   0 
        right = len(matrix[0]) - 1 
        top = 0 
        bottom = len(matrix) - 1
        while left <= right and top<=bottom :
             for i in range (left , right+1):
                result.append(matrix[top][i])
             top +=1
             for j in range (top , bottom + 1 ) :
                result.append(matrix[j][right])
             right -= 1
             if top <= bottom :
                for k in range(right ,left -1 , -1):
                    result.append(matrix[bottom][k])
                bottom -=1
             if left <= right :
                for m in range (bottom , top - 1 , -1):
                    result.append(matrix[m][left])
                left +=1
        return result