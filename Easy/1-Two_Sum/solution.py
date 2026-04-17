class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        my_dict={}
        for i, num in enumerate(nums):
            complement = target - num
            if complement in my_dict:
                return [my_dict[complement], i]
            my_dict[num] = i
                