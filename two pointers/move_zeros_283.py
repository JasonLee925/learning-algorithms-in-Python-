# given:
nums = [0,1,0,3,12]

# answer:
p = 0
for i, x in enumerate(nums):
    if x != 0:
        tmp = nums[i]
        nums[i] = nums[p]
        nums[p] = tmp
        p+=1
            

print(nums)