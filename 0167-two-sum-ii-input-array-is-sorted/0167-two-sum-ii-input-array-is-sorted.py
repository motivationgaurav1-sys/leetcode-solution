class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        """seen={}
        for a in range(len(numbers)):
            need =target-numbers[a]
            if need in seen:
                return [seen[need]+1,a+1]
            seen[numbers[a]]=a """  
        i=0
        j=len(numbers)-1
        while i<j:
            if (numbers[i]+numbers[j])==target:
                return [i+1,j+1]
            elif (numbers[i]+numbers[j])<target:
                i+=1
            else:
                j-=1

