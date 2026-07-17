class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if not s or not t:
            return False
        ls = list(s)
        lt = list (t)
        ls.sort()
        lt.sort()
        if len(ls) != len(lt):
            return False
        else:
            for i in range(len(ls)):
                if ls[i]== lt[i]:
                    i +=1
                else:
                    return False
            return True
        
