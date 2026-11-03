class Solution(object):
    def setZeroes(self, matrix):
        r=len(matrix)
        c=len(matrix[0])
        row=[-1]*r
        col=[-1]*c
        for i in range(r):
            for j in range(c):
                if(matrix[i][j]==0):
                    row[i]=0
                    col[j]=0
        
        for i in range(r):
            for j in range(c):
                if((row[i]==0 or col[j]==0) and matrix[i][j]!=0):
                    matrix[i][j]=0

        return matrix
        