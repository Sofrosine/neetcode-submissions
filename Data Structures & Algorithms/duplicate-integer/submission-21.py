class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        if len(nums):
            nums.sort()
            num = nums.pop(0)
            for index,value in enumerate(nums):
                if index < len(nums):
                    if num == nums[index]:
                        return True
                    else:
                        num = nums[index]
                    


        return False
        