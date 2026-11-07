class Solution(object):
    def sumOddLengthSubarrays(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        sums=sum(arr)

        for a in range(len(arr)):
            for b in range(a+1,len(arr)):
                if len(arr[a:b+1])%2!=0:
                    sums+=sum(arr[a:b+1])
        return sums            
        