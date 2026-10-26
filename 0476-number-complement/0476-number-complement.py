class Solution(object):
    def findComplement(self, num):
        """
        :type num: int
        :rtype: int
        """
        # we have to make it if binary is one change it to 0 and if 0 than to 1 
        #first find binary
        binary=""
        while num>0:
            if num%2==0:
                binary+="0"
            else:
                binary+="1"
            num//=2
        binary=binary[::-1]    
        complement=""        
        for i in binary:
            if i=="0":
                complement+="1"
            else:
                complement+="0"
        return int(complement,2)                        