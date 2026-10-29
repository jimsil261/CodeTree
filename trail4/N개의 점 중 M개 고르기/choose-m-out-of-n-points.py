n, m = map(int, input().split())
points = [tuple(map(int, input().split())) for _ in range(n)]

# Please write your code here.
picked = []
answer= float("inf")

def calculate():
    max_distance=0
    for i in range(len(picked)):
        for j in range(i+1,len(picked)):
            max_distance=max(pow(picked[j][1]-picked[i][1],2)+pow(picked[j][0]-picked[i][0],2),max_distance)
    return max_distance

def choose(idx, count):
    global answer

    if count == m:
        answer=min(answer,calculate())
        return

    if idx == n:
        return

    picked.append(points[idx])
    choose(idx+1,count+1)
    picked.pop()
    choose(idx+1,count)


choose(0, 0)
print(answer)
