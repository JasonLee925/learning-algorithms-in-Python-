# given:
nums = [0,1,0,3,12]
k = 3

# answer:
for _ in range(k):
    end = nums.pop()
    nums.insert(0, end)
        
print(nums)


#--
# some says this is dumb, but I dont care. This the first question I finished without refering tutorials.
# Dont be too PC:)