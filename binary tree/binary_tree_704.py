# given:
nums = [-1, 1, 5, 7, 10, 18]
target = 101

# answer:
ans = -1
begin = 0
end = len(nums) - 1

while begin <= end:
    pivot = (end - begin) // 2 + begin
    if target > nums[pivot]:
        begin = pivot + 1
    elif target < nums[pivot]:
        end = pivot - 1
    else: 
        ans = pivot
        break

print(ans)