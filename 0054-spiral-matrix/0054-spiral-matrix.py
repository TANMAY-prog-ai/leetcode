class Solution(object):
    def spiralOrder(self, matrix):
        n=len(matrix)
        a=len(matrix[0])
        srow=0
        erow=n-1
        scol=0
        ecol=a-1
        final=[]
        while(srow<=erow and scol<=ecol):
            for i in range(scol,ecol+1):
                final.append(matrix[srow][i])

            for j in range(srow+1,erow+1):
                final.append(matrix[j][ecol])

            for k in range(ecol-1,scol-1,-1):
                if srow < erow:
                    final.append(matrix[erow][k])
        
            for l in range(erow-1,srow,-1):
                if scol < ecol:
                    final.append(matrix[l][scol])
            srow+=1
            erow-=1
            scol+=1
            ecol-=1
        
        return final