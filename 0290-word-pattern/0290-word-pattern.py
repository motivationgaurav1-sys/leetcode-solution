class Solution(object):
    def wordPattern(self, pattern, s):
        """
        :type pattern: str
        :type s: str
        :rtype: bool
        """
        words=s.split()
        if len(pattern)!=len(words):
                return False
        char_to_word={}
        word_to_char={}
        for a,b in zip(pattern,words):
            if a in char_to_word and char_to_word[a]!=b:
                return False
            if b in word_to_char and word_to_char[b]!=a:
                return False

            char_to_word[a]=b
            word_to_char[b]=a
        return True        

        


                    

                    


        