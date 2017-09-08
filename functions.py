import sys
# Solution to problem 10; fibonacci
def iter_fib(num):
    # Keeps track of the number, what number to add next,
    # and specifically a temporary holder for switching things up
    # fibonacci is tricky because you don't want to overwrite
    currentNum = 1
    prevNum = 0
    temp = 0

    # how do defaults even work \o/
    if num == None:
        num = 10

    # basic loop for fibonacci. As an example, let's say we're at 1 2 3 5
    # take whatever number is up, add the previous number. (5+3, next num is 8)
    # temp holds the previous number to add to the new number (temp = 3)
    # load up the new previous number (the new prevnum is now 5)
    # now load up the new current number (we're moving onto 3+5 or 8)
    for i in range(num):
        print currentNum+prevNum
        temp = prevNum
        prevNum = currentNum
        currentNum = temp+currentNum

# I'm not sure about defaults yet

num = 10
if len(sys.argv) == 2:
    num = int(sys.argv[1])

#iter_fib(num)

# Recursion!
def recur_factorial(num_factorial):
    # End of the line; important unless we wanna infinite loop
    if num_factorial == 1:
        return 1
    # Not quite done yet; do another call of the function
    # It basically calls another function of itself over and over until 1
    else:
        return num_factorial * recur_factorial(num_factorial-1)

print recur_factorial(3)
