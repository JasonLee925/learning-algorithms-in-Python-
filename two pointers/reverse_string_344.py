# given:
s = ["h","e","l","l","o"]

# answer:
fi = 0           # first
ei = len(s)-1 # end

b = 0
e = len(s) - 1
while e > b:
    tmp = s[b] 
    s[b] = s[e]
    s[e] = tmp
    
    b += 1
    e -= 1

print(s)