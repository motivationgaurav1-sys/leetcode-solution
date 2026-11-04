class Solution(object):
    def flipAndInvertImage(self, image):
        """
        :type image: List[List[int]]
        :rtype: List[List[int]]
        """
        
        """for i in range(len(image)):
            a=0
            b=len(image)-1
            while a<b:
                image[i][a],image[i][b]=image[i][b],image[i][a]
                a+=1
                b-=1
        result=[]
        for j in image:
            new_row=[]
            for k in j:
                if k==0:
                    new_row.append(1)
                else:
                    new_row.append(0)
            result.append(new_row)            
        return result"""
        for row in image:
            row.reverse()
            for i in range(len(image)):
                row[i]^=1
        return image    
        """for  row in image:
            row.reverse()
            for i in range(len(image)):
                row[i]=1-row[i]
        return image"""        
                




        