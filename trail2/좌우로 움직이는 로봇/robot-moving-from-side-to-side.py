n, m = map(int, input().split())

# Process robot A's movements
t = []
d = []
for _ in range(n):
    time, direction = input().split()
    t.append(int(time))
    d.append(direction)

# Process robot B's movements
t_b = []
d_b = []
for _ in range(m):
    time, direction = input().split()
    t_b.append(int(time))
    d_b.append(direction)

# Please write your code here.
pos_a = [0]
pos_b = [0]
answer = 0

for i in range(n):
    if d[i]=="L":
        for j in range(t[i]):
            pos_a.append(pos_a[-1]-1)
    else:
        for j in range(t[i]):
            pos_a.append(pos_a[-1]+1)

for i in range(m):
    if d_b[i]=="L":
        for j in range(t_b[i]):
            pos_b.append(pos_b[-1]-1)
    else:
        for j in range(t_b[i]):
            pos_b.append(pos_b[-1]+1)

if len(pos_a)>len(pos_b):
    for i in range(len(pos_a)-len(pos_b)):
        pos_b.append(pos_b[-1])
else:
    for i in range(len(pos_b)-len(pos_a)):
        pos_a.append(pos_a[-1])


for second in range(1, len(pos_a)):
    if pos_a[second-1]!=pos_b[second-1] and pos_a[second]==pos_b[second]:
        answer+=1

print(answer)