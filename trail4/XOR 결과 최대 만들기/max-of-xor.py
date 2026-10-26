n, m = map(int, input().split())
A = list(map(int, input().split()))

# Please write your code here.
answer=0

def choose(start, count, xor_value):
    global answer

    if count==m:
        answer=max(answer,xor_value)
        return
    if start==n:
        return

    choose(start+1,count+1,xor_value ^ A[start])

    choose(start+1,count,xor_value)

choose(0,0,0)
print(answer)