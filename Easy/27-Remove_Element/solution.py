class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        first = 0
        last = len(nums) - 1 
        while first <= last:
            if nums[first] == val:
                nums[first] = nums[last]
                last -= 1
            else:
                first += 1           
        return first