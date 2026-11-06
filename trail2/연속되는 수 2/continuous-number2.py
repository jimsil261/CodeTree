n = int(input())
arr = [int(input()) for _ in range(n)]

# Please write your code here.
max_count=0
count=0
for i in range(n):
    if i==0 or arr[i]!=arr[i-1]:
        max_count=max(max_count,count)
        count=1
    else:
        count+=1
max_count = max(max_count, count)
print(max_count)
