class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numss=[]
        for k in range(len(nums)):
            numss.append([nums[k],k])
        nums_s=sorted(numss)
        T=False
        for i in range(len(nums)):
            for j in range((len(nums)-1),i,-1):
                if nums_s[i][0]+nums_s[j][0]==target:
                    answers=[nums_s[i][1],nums_s[j][1]]
                    T=True
                    return sorted(answers)
                    break
                elif nums_s[i][0]+nums_s[j][0]>target:
                    continue
                elif nums_s[i][0]+nums_s[j][0]<target:
                    break
            if T:
                break


                
