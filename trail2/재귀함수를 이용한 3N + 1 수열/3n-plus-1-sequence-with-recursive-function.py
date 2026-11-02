n = int(input())

# Please write your code here.
def count_steps(number):
    if number==1:
        return 0

    if number % 2 == 0:
        return 1+ count_steps(number//2)
        
    else:
        return 1+count_steps(3*number+1)


print(count_steps(n))