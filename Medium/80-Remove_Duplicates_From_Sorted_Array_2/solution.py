class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        cnt = 1
        how_many=1
        moving = 1
        if len(nums)==0:
            return 0
        while moving <= len(nums)-1:
            if nums[cnt-1] == nums[moving]:
                how_many+=1
                if how_many <= 2:
                    nums[cnt]=nums[moving]
                    cnt+=1
            else:
                nums[cnt]=nums[moving]
                how_many=1
                cnt+=1
            moving +=1
        return cnt