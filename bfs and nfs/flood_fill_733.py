# given:
image = [[1,1,1],[1,1,0],[1,0,1]]
sr = 1
sc = 1
newColor = 2

# answer (BFS):
def adjacent(l):
    return [
        [l[0]-1, l[1]],
        [l[0]+1, l[1]],
        [l[0], l[1]-1],
        [l[0], l[1]+1],
    ]

m = len(image)-1
n = len(image[sr])-1
tc = image[sr][sc]
visited = []
nxt2visit = [[sr,sc]]

while len(nxt2visit) != 0:
    tn = nxt2visit.pop()
    
    if tn in visited:
        continue
    
    if image[tn[0]][tn[1]] == tc:
        image[tn[0]][tn[1]] = newColor
        
    visited.append(tn)
    
    for v in adjacent(tn):
        if v[0] < 0 or v[1] < 0 or v[0] > m or v[1] > n:
            continue
        if image[v[0]][v[1]] != tc:
            continue
        nxt2visit.append(v)
    

print(image) # expected = [[2,2,2],[2,2,0],[2,0,1]]