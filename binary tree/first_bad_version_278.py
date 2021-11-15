def isBadVersion(t):
    return t >= 5

def firstBadVersion(n):
    ans = 1
    begin = 1
    end = n
    
    while begin < end:
        pv = (end - begin) // 2 + begin
        
        if isBadVersion(pv):
            end = pv
        else:
            begin = pv + 1 # why +1 here?
            # bc when 'pv' is Good, meaning that 'pv' itself  including that of smaller numbers are all Good.
            # So we should move on (+1) to the next number, which might be Bad, to keep searching.
        ans = begin

    return ans

print(firstBadVersion(6))
