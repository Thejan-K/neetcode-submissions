class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dic={}
        answers=[]
        for num in nums:
            if num in dic:
                dic[num]+=1
            else:
                dic[num]=1
        for i in range(k):
            max_key=max(dic, key=dic.get)
            answers.append(max_key)
            del dic[max_key]
        return answers
