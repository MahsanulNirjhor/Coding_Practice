class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        #if not nums: return []
        
        result = []
        nums.sort()
        
        
        for i,n in enumerate(nums):
            #print(f'nums[i-1] : {nums[i-1]}   n : {n}')
            if i > 0 and n == nums[i-1]:
                continue
                
            l = i+1
            r = len(nums) - 1
            #print(nums)
            while l < r :
                comb = n + nums[l] + nums[r]
                #print(comb)
                if comb > 0 :
                    r-=1
                elif comb < 0 :
                    l+=1
                else:
                    #if [n,nums[l],nums[r]] not in result:
                    result.append([n,nums[l],nums[r]])
                    l+=1
                    while nums[l-1] == nums[l] and l < r :
                        l += 1
                        
        return result