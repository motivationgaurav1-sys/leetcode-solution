class Solution(object):
    def transpose(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[List[int]]
        """
        a=0  
        result=[]  
        for i in range(len(matrix[0])):
            new_row=[]
            for j in range(len(matrix)):

            
                new_row.append(matrix[j][a])
            a+=1    
            result.append(new_row)
        return result            


        

            