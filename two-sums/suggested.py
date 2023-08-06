def twoSum(nums, target):
    diff_dict={}
    for i in range(len(nums)):
        difference = target -nums[i]
        if difference in diff_dict:
            return[diff_dict[difference],i]
        else:
            diff_dict[nums[i]]=i