a, b, c = map(int, input().split())

# Please write your code here.
def digit_sum(number):
    if number<10:
        return number
    else:
        return number%10 + digit_sum(number//10)

print(digit_sum(a*b*c))