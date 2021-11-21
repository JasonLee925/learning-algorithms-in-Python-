# given:
s = "Let's take LeetCode contest"

# answers 1 (my first solution):
def reverse(l:list) -> list:
    b = 0
    e = len(l) - 1
    while e > b:
        tmp = l[b] 
        l[b] = l[e]
        l[e] = tmp

        b += 1
        e -= 1
    return l

sl = []
sl[:0] = s
sl = reverse(sl)
sl = ''.join(sl)

ssl = sl.split(' ')
ssl = reverse(ssl)
print(' '.join(ssl))
    
# answer 2 (faster)
ans = []
for i in s.split():
    i = i[::-1]
    ans.append(i)
print(" ".join(ans))
# or either ...
# print(" ".join([i[::-1] for i in s.split()]))

