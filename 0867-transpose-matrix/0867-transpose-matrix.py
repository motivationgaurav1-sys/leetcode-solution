class Solution(object):
    def transpose(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[List[int]]
        """
        """a=0  
        result=[]  
        for i in range(len(matrix[0])):
            new_row=[]
            for j in range(len(matrix)):

            
                new_row.append(matrix[j][a])
            a+=1    
            result.append(new_row)
        return result """   
        rows=len(matrix)
        cols=len(matrix[0])
        result=[[0]*rows for i in range(cols)]
        for i in range(rows):
            for j in range(cols):
                result[j][i]=matrix[i][j]
        return result                


        

            