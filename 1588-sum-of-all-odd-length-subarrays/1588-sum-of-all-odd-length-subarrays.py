class Solution(object):
    def sumOddLengthSubarrays(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        """sums=sum(arr)

        for a in range(len(arr)):
            for b in range(a+1,len(arr)):
                if len(arr[a:b+1])%2!=0:
                    sums+=sum(arr[a:b+1])
        return sums   """
        total=0
        for a in range(len(arr)):
            current_sum=0 
            for b in range(a,len(arr)):
                current_sum+=arr[b]
                if (b-a+1)%2!=0:
                    total+=current_sum   
        return total