n, m = map(int, input().split())

d = []
t = []
for _ in range(n):
    direction, time = input().split()
    d.append(direction)
    t.append(int(time))

d2 = []
t2 = []
for _ in range(m):
    direction, time = input().split()
    d2.append(direction)
    t2.append(int(time))

# Please write your code here.
pos_a = [0]
pos_b = [0]
answer = -1

for i in range(n):
    if d[i]=="R":
        for j in range(t[i]):
            pos_a.append(pos_a[-1]+1)
    else:
        for j in range(t[i]):
            pos_a.append(pos_a[-1]-1)

for i in range(m):
    if d2[i]=="R":
        for j in range(t2[i]):
            pos_b.append(pos_b[-1]+1)
    else:
        for j in range(t2[i]):
            pos_b.append(pos_b[-1]-1)

for second in range(1, len(pos_a)):
    if pos_a[second]==pos_b[second]:
        answer=second
        break

print(answer)