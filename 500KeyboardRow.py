class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        a=set('qwertyuiop')
        b=set('asdfghjkl')
        c=set('zxcvbnm')
        result=[]
        
        for word in words:
            t=set(word.lower())
            if a & t == t:         
#a = set('qwertyuiop')
#b = set('asdfghjkl')
#c = set('dad')
# a&c
#set([])
#a&c == c
#False
#b&c == c
#True
                result.append(word)
            if b & t == t:
                result.append(word)
            if c & t == t:
                result.append(word)
        return result
