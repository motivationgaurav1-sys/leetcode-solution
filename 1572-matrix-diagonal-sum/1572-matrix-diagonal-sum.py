class Solution(object):
    def diagonalSum(self, mat):
        """
        :type mat: List[List[int]]
        :rtype: int
        """   
       
        """l2=[]
        l3=[]
        p=len(mat)-1
        k=0
        n=len(mat)
        for i in range(len(mat)):
            l2.append(mat[i][k])
            k+=1
        for j in range(len(mat)):
            l3.append(mat[j][p])
            p-=1
        l2.extend(l3)
        a=sum(l2)    
        if len(mat)%2!=0:
            a=a-mat[n//2][n//2]
        return a    
"""
        n=len(mat)
        total=0
        for i in range(n):
            total+=mat[i][i]
            if i!=n-1-i:
                total+=mat[i][n-1-i]
        return total        
               


