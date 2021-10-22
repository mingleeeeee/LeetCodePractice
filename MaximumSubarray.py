class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        sum, max = nums[0], nums[0]
        
        for i in range(1, len(nums)):
            if nums[i] > sum+nums[i]:
                sum = nums[i]
            else:
                sum = sum+nums[i]
            
            if sum>max:
                max=sum
        return max