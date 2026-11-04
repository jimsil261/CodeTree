n = int(input())
arr = list(map(int, input().split()))

# Please write your code here.
def gcd(a, b):
    # 두 수의 최대공약수
    if b==0:
        return a
    else:
        return gcd(b,a%b)


def lcm(a, b):
    # 두 수의 최소공배수
    return a*b//gcd(a,b)


def lcm_all(count):
    if count==1:
        return arr[0]
    previous_lcm = lcm_all(count - 1)
    return lcm(previous_lcm, arr[count - 1])


print(lcm_all(n))