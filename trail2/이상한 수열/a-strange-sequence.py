N = int(input())

# Please write your code here.
def sequence(n):
    if n==1:
        return 1
    elif n==2:
        return 2
    else:
        return sequence(n//3)+sequence(n-1)


print(sequence(N))