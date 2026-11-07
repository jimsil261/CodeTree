n, m = map(int, input().split())

# Process A's movements
v = []
t = []
for _ in range(n):
    vi, ti = map(int, input().split())
    v.append(vi)
    t.append(ti)

# Process B's movements
v2 = []
t2 = []
for _ in range(m):
    vi, ti = map(int, input().split())
    v2.append(vi)
    t2.append(ti)

# Please write your code here.
pos_a = [0]
pos_b = [0]
answer = 0
leader = 0  # 0은 아직 선두 없음, 1은 A, 2는 B

# A의 매초 위치 기록
for i in range(n):
    for j in range(t[i]):
        pos_a.append(pos_a[-1]+v[i])

# B의 매초 위치 기록
for i in range(m):
    for j in range(t2[i]):
        pos_b.append(pos_b[-1]+v2[i])

for second in range(1, len(pos_a)):
    if leader==0:
        if pos_a[second]>pos_b[second]:
            leader=1

        elif pos_a[second]<pos_b[second]:
            leader=2

    elif leader==1:
        if pos_a[second]<pos_b[second]:
            leader=2
            answer+=1
    else:
        if pos_a[second]>pos_b[second]:
            leader=1
            answer+=1


print(answer)