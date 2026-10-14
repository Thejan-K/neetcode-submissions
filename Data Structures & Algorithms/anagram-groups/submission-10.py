class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dic={}
        finalist=[]
        for string in strs:
            sortedS=''.join(sorted(string))
            if sortedS not in dic:
                dic[sortedS]=[string]
            else:
                dic[sortedS].append(string)
        for s in dic:
            finalist.append(dic[s])
        return finalist
                    