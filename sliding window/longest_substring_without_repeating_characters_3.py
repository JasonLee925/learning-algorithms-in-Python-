# given:
s = "abcabcbb" #3
# s = "bbbbb" #1
# s = "pwwkew" #3
# s = "dfdv" #3
# s = "" #0

# answer:
tmp = []
ans = 0

for c in list(s):
    if c in tmp:
        ti = tmp.index(c)+1 # find the corresponding index in tmp list.
        tmp = tmp[ti:] # trim the tmp list with the index of the char in the list itself.
    tmp.append(c) # append new char whatever happens

    if ans < len(tmp): # check the length of current tmp list 
        ans = len(tmp) # if greater than current answer, change the answer.

print(ans)