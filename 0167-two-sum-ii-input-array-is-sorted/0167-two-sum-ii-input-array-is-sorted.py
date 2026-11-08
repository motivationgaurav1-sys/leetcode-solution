class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        seen={}
        for a in range(len(numbers)):
            need =target-numbers[a]
            if need in seen:
                return [seen[need]+1,a+1]
            seen[numbers[a]]=a   
