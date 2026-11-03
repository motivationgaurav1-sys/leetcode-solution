class Solution(object):
    def isIsomorphic(self, s, t):
        if len(s)!=len(t):
            return False
        dict1,dict2={},{}    
        for a,b in zip(s,t):
            if a in dict1 and dict1[a]!=b:
                return False
            if b in dict2 and dict2[b]!=a:
                return False    
            dict1[a],dict2[b]=b,a
        return True     
