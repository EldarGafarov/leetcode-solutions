class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        res=[0]*len(nums)
        left_lst=[1]*len(nums)
        right_lst=[1]*len(nums)
        for i in range(len(nums)-1):
            left_lst[i+1]=left_lst[i]*nums[i]
        for j in range((len(nums)-1),0,-1):
            right_lst[j-1]=right_lst[j]*nums[j]
        for k in range(len(nums)):
            res[k]=left_lst[k]*right_lst[k]
        return res