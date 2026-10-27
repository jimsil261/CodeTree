n = int(input())
grid = [list(input()) for _ in range(n)]

# Please write your code here.
coins=[]
start=None
end=None
answer=float("inf")

def distance(pos1,pos2):
    return(abs(pos1[0]-pos2[0])+abs(pos1[1]-pos2[1]))

def choose(idx,count,current,total_distance):
    global answer
    if idx==len(coins):
        if count>=3:
            answer=min(answer, total_distance+distance(current,end))
        return
    coin_pos = (coins[idx][1], coins[idx][2])

    choose(idx + 1, count + 1, coin_pos,
        total_distance + distance(current, coin_pos))

    choose(idx + 1, count, current, total_distance)

for i in range(n):
    for j in range(n):
        if grid[i][j]=="S":
            start=(i,j)
        elif grid[i][j]=="E":
            end=(i,j)
        elif grid[i][j].isdigit():
            coins.append((int(grid[i][j]),i,j))
coins.sort()

choose(0, 0, start, 0)
print(-1 if answer == float("inf") else answer)