class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        j= len(nums) -1
        ol = []
        for i in range(len(nums)-1):
            for j in range(i+1,len(nums)):
                if nums[i] + nums[j] == target:
                    ol.append(i)
                    ol.append(j)
                    return ol
                else:
                    j -=1
            i +=1
        return []
        

