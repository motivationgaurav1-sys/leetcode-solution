class Solution(object):
    def containsDuplicate(self, nums):
       # return len(nums)!=len(set(nums))
        my_set=set(nums)
        if len(my_set)==len(nums):
            return False
        else:
            return True    


        