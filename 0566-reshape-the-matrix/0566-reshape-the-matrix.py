class Solution(object):
    def matrixReshape(self, mat, r, c):
        """
        :type mat: List[List[int]]
        :type r: int
        :type c: int
        :rtype: List[List[int]]
        """
        """rows=len(mat)
        column=len(mat[0])
        if rows*column!=r*c:
            return mat
        else:
            orignal=[]
            for row in mat:
                for value in row:
                    orignal.append(value)

            result=[]
            k=0
            for i in range(r):
                new_row=[]
                for j in range(c):
                    new_row.append(orignal[k])
                    k+=1
                result.append(new_row)

        return result            
"""
        rows=len(mat)
        columns=len(mat[0])
        if rows*columns!=r*c:
            return mat
        values=[]
        for row in mat:
            values.extend(row)
        result=[]
        for i in range(r):
            result.append(values[i*c:(i+1)*c])    

        return result