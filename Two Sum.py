def Two_sum(nums, target):
    for i in range(len(nums)):
        for j in range(i+1,len(nums)):
            if nums[i]==nums[j]:
                continue
            elif nums[i] + nums[j] == target:
                print(i, j)


Two_sum(nums=[1,2,3,4,5], target=6)
