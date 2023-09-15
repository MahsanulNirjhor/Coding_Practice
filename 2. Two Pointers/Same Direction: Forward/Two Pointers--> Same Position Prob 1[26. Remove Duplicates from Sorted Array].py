class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        l = 1 
        
        for r in range(1,len(nums)):
            if nums[r-1] != nums[r]:
                nums[l] = nums[r]
                l+= 1
                
        return l
        
        
        """"
        Version 1 my own doing
        l = 1
        r = 1
        
        while r < len(nums):
            if nums[r-1] == nums[r]:
                r+=1
            elif nums[r-1] != nums[r]:
                nums[l]=nums[r]
                l+=1
                r+=1
                
                
        return l
        """
        