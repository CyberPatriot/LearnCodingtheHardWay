#Declare string x
x = "There are %d types of people." % 10 #No argument is converted, results in a '%' character in the result.

#Declare String binary
binary = "binary"

#Declare String  do_not
do_not = "don't"

#Declare String y
y = "Those who know %s and those who %s." % (binary, do_not) ### String within a string

#pint strings x and y
print x
print y

#print strings x & y AS IS with %r and with string only %s
print "I said: %r." % x ### String within a string
print "I also said: '%s'." % y ### String within a string

#define bool and strings
hilarious = False
joke_evaluation = "Isn't that joke so funny?! %r"

#print above ^
print joke_evaluation % hilarious ### String within a string due to above %r ^

# declare strings w and e
w = "This is the left side of..."
e = "a string with a right side."

#string print with concat of strings ( + )
print w + e
