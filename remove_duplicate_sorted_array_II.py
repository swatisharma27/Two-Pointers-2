class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        '''
        Removes duplicates, at the most can have two duplicates 

        Return count of elements after removing duplicates with at the most two duplicates

        TC: O(n)
        AS : O(1)
        '''

        if not nums:
            return 0

        left = 1
        right = 1
        count = 1
        k = 2

        for right in range(1, len(nums)):

            if nums[right] == nums[right-1]:
                count += 1
            else:
                count = 1
            
            if count <= k:
                nums[left] = nums[right]
                left += 1

        return left

if __name__ == "__main__":  
    nums = [0,0,1,1,1,1,2,3,3]
    s = Solution()
    print(s.removeDuplicates(nums))
