class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count_dict = dict()
        for num in nums:
            count_dict[num] = count_dict.get(num,0)+1
        result = max(count_dict, key=count_dict.get)
        return result
        