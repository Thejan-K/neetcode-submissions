class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sdic={}
        for chars in s:
            if chars in sdic:
                sdic[chars]+=1
            else:
                sdic[chars]=1
        tdic={}
        for chart in t:
            if chart in tdic:
                tdic[chart]+=1
            else:
                tdic[chart]=1
        if len(sdic)>len(tdic):
            longdic=sdic
            shortdic=tdic
        else:
            longdic=tdic
            shortdic=sdic
        for char1 in longdic:
            T=False
            for char2 in shortdic:
                if char1==char2:
                    if sdic[char1]==tdic[char2]:
                        T=True
                        break
                    else:
                        return False
                else:
                    continue
            if not T:
                return False
        return True
                
        