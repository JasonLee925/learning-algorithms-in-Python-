# given:
nums = [2,7,11,15]
t = 9 # t

# answer:
# slower answer:
#         diffs = []
#         for i, v in enumerate(numbers):
#             d = t - v
#             if d not in diffs:
#                 diffs.append(v)
#             else:
#                 x = diffs.index(d) +1 
#                 y = i + 1
#                 return [x, y]
   
# a little bit faster answer:                     
bi = 0
ei = len(nums) - 1

while bi < ei:
    if nums[bi] + nums[ei] > t:
        ei-=1
    elif nums[bi] + nums[ei] == t:
        bi+=1
        ei+=1
        break 
    else:
        bi+=1
                
                
            
print([bi, ei])

# excepted: [1,2]
