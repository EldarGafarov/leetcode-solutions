class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        cnt = 0
        moving = 1
        if len(nums)==0:
            return 0
        while moving <= len(nums)-1:
            if nums[cnt] == nums[moving]:
                moving +=1
            else:
                nums[cnt+1]=nums[moving]
                moving+=1
                cnt+=1
        return cnt+1