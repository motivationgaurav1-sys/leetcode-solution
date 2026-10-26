class Solution(object):
    def reverse(self, x):
            negative=x<0
            x=abs(x)
            reverse=int(str(x)[::-1])
            if negative:
                reverse=-reverse
            if -2**31<=reverse<=2**31-1:
                return reverse
            else:
                return 0       