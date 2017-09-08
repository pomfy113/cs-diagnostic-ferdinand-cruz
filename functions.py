# Solution to problem 10; fibonacci
def iter_fib(num):
    # Keeps track of the number, what number to add next,
    # and specifically a temporary holder for switching things up
    currentNum = 1
    prevNum = 0
    temp = 0

    # how do defaults even work \o/
    if num == None:
        num = 10

    # basic loop for fibonacci
    # take whatever number is up, add the prev
    for i in range(num):
        print currentNum+prevNum
        temp = prevNum
        prevNum = currentNum
        currentNum = temp+currentNum

# I'm not sure about defaults yet
num = 10
iter_fib(num)
