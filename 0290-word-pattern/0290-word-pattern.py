class Solution(object):
    def wordPattern(self, pattern, s):
        words=s.split()
        if len(pattern)!=len(words):
            return False
        forward, backward={},{}
        for char, word in zip(pattern,words):
            if char in forward and forward[char]!=word:
                return False
            if word in backward and backward[word]!=char:
                return False
            forward[char],backward[word]=word,char
        return True                    

        


                    

                    


        