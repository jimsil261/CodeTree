N, M = map(int, input().split())

# Please write your code here.
picked=[]

def choose(start,count):
    if start==N+1:
        if count==M:
            print(*picked)
        return
    picked.append(start)
    choose(start+1,count+1)
    picked.pop()

    choose(start+1,count)
    return
choose(1,0)
