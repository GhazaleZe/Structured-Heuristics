class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        nums.sort()
        print(nums)
        ll =len(nums)
        if ll == 1:
            return nums[0]
        else:
            for i in range(len(nums)-1):
                if nums[i] == nums[i+1] or nums[i] == nums[i-1]:
                    continue
                else:
                    return nums[i]
            if nums[ll-1] != nums [ll -2]:
                return nums [ll -1]
        



        