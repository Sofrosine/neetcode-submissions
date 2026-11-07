class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        if len(nums):
            arr = nums.copy()
            arr.sort()
            num = arr.pop(0)
            print(arr)
            for index,value in enumerate(arr):
                if index < len(arr):
                    if num == arr[index]:
                        return True
                    else:
                        num = arr[index]
                    


        return False
        