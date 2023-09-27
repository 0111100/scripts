# 316. Remove Duplicate Letters

class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        a=[]
        
        for i in range(len(s)):
           
            if(s[i] not in a):
                l=len(a)-1
               
                while(l>=0 and a[l]>s[i] and a[l] in s[i+1:]):
                    a.pop()
                    l-=1
                a.append(s[i])
                
        a="".join(a)
        return(a)
