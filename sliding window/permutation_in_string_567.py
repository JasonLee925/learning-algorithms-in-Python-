# given:
s1= "adc"
s2= "dcda"

# answer:
ans = False
def f(c):
    return ord(c) - 97

ct_s, ct_p = [0] * 26, [0] * 26
for c in s1:
    ct_p[f(c)] += 1

l = len(s1) - 1
for c in s2[:l]:
    ct_s[f(c)] += 1
    
for i, c in enumerate(s2[l:]):
    ct_s[f(c)] += 1
    if ct_s == ct_p:
        ans = True
    ct_s[f(s2[i])] -= 1

print(ans)