N, M, K = map(int, input().split())
student = [int(input()) for _ in range(M)]

# Please write your code here.
answer=-1
arr=[K]*N
for i in student:
    arr[i-1]-=1
    if arr[i-1]==0:
        answer=i
        break
print(answer)