class Solution(object):
    def hammingWeight(self, n):
        reminder=""
        count=0
        while n!=0:
            if n%2==0:
                reminder+="0"
            else:
                reminder+="1"
            n=n//2    
        for i in reminder:
            if i=="1":
                count+=1  
        return count                  
        