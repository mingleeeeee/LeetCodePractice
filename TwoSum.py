class Solution(object):
    def twoSum(self, nums, target):
        length = len(nums)
        ans=[]
        for i in range(0,length):
            for j in range(i+1, length):
                if (nums[j] == target - nums[i]):
                    ans.append(i)
                    ans.append(j)
                    return ans
                
# Brute Force: O(n^2)