import sys

# Grab the input; first, where you want a set of numbers to start, then
# where you want it to end. Check if divisible by 3 and 5 (15), type fizzbuzz.
# (means it's divisible by BOTH 3 and 5)
# Otherwise, if divisible by 3, type fizz. If by 5, buzz.

# just to make it easier to see how long it needs to go
# grabs the 2nd and 3rd element and uses them as thresholds
listLen = int(sys.argv[2]) - int(sys.argv[1])+1

for i in range(listLen):
    if (int(sys.argv[1])+i) % 15 == 0:
        print "fizzbuzz"
    elif (int(sys.argv[1])+i) % 3 == 0:
        print "fizz"
    elif (int(sys.argv[1])+i) % 5 == 0:
        print "buzz"
    else:
        print int(sys.argv[1])+i

# There's more efficient ways of doing this
# with outside help, probably some way to make sys.argv[1]+i not be repeated
# There's also the matter of just removing the number and appending fizz/buzz
# or both depending on what matches
