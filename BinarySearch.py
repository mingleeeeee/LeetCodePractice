class Solution:
    def search(self, nums: List[int], target: int) -> int:
        low, up=0, len(nums)-1
        while(low<=up):
            m= (low+up)//2
            if nums[m]==target:
                return m
            elif nums[m] < target:
                low=m+1
            elif nums[m] > target:
                up=m-1
        return -1