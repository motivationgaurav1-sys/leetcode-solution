class Solution(object):
    def findLucky(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        a=0
        freq={}
        for i in arr:
            freq[i]=freq.get(i,0)+1
        ans=-1    
        for k,v in freq.items():
            if k==v:
                if k>ans:
                    ans=k
        return ans               

        """l2=[]
        for i in arr:
            if arr.count(i)==i:
                l2.append(i)
        if len(l2)!=0:
            return max(l2)
        else:
            return -1 """           



        