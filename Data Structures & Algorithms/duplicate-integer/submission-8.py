class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        if len(nums):
            arr = nums.copy()
            arr.sort()
            num = arr[0]
            print(str(arr))
            for index,value in enumerate(arr):
                print(str(index) + " " +str(num))
                if index < len(arr)-1:
                    if num == arr[index+1]:
                        return True
                    else:

                        num = arr[index+1]
                    


        return False
        