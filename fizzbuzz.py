n = 0

for n in xrange(1, 101):
    if n % 15 == 0:
        print "FizzBuzz"
    elif n % 3 == 0:
        print "Fizz"
    elif n % 5 == 0:
        print "Buzz"
    else:
        print n
        
        


