# given:
nums = [-1, 1, 5, 7, 10, 18]
target = 10

# answer:
begin = 0
end = len(nums)-1

while begin <= end:
    p = (end - begin)//2 + begin
    
    if nums[p] > target:
        end = p - 1
    elif nums[p] < target:
        begin = p + 1
    else:
        begin = p
        break
    

print(begin)