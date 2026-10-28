n = int(input())
num = list(map(int, input().split()))

# Please write your code here.
answer=float("inf")
total_sum=sum(num)

def choose(idx,count,selected_sum):
    global answer
    if count == n:
        answer = min(answer, abs(selected_sum - (total_sum - selected_sum)))
        return

    if idx==len(num):
        return
    choose(idx+1,count+1,selected_sum+num[idx])

    choose(idx+1,count,selected_sum)

choose(0,0,0)
print(answer)