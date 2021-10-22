class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        left, right= 0, len(nums)-1
        
        if nums[left] > target:
            return left
        if nums[right] < target:
            return right+1
        while(left <= right):
            pivot= (left+right)//2
            if ( nums[pivot] == target):
                return pivot
            elif nums[pivot] > target:
                if nums[pivot-1] < target:
                    return pivot
                else:
                    right = pivot-1
            elif nums[pivot] < target:
                if nums[pivot+1] > target:
                    return pivot+1
                left = pivot+1