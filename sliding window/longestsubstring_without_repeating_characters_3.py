# given:
s = "abcabcbb" #3
# s = "bbbbb" #1
# s = "pwwkew" #3
# s = "dfdv" #3
# s = "" #0

# answer:
tmp = []
ans = 0

for v in list(s):
    if v in tmp:
        ti = tmp.index(v)+1
        tmp = tmp[ti:]
    tmp.append(v)
    if ans < len(tmp):
        ans = len(tmp)

print(ans)