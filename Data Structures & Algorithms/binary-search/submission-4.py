class Solution:
    def search(self, nums: List[int], target: int) -> int:
        low = 0
        high = len(nums) - 1
        while low <= high:
            mid = (low + high) // 2
            val = nums[mid]
            print("value" + str(val))
            print("mid index" + str(mid))
            if val == target:
                return mid
            elif val > target:
                high = mid - 1
            elif val < target:
                low = mid + 1

        return -1