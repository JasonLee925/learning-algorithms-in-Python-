# given:
nums = [-7,-3,2,3,11]

# answer:
ans = []
fi = 0           # first
ei = len(nums)-1 # end

for i in range(len(nums)):
    if abs(nums[fi]) > abs(nums[ei]):
        ans.insert(0, nums[fi]**2)
        fi += 1
    else:
        ans.insert(0, nums[ei]**2)
        ei -= 1
            

print(ans)