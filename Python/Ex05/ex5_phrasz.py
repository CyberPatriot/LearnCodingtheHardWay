name = 'Zed A. Shaw'
age = 35 # not a lie
height = 74 # inches
weight = 180 # lbs
eyes = 'Blue'
teeth = 'White'
hair = 'Brown'

inches = 2.5
cm = 0.0

kilos = 7.5

print "Let's talk about %s." % name
print "He's %d inches tall." % height
print "He's %d pounds heavy." % weight
print "Actually that's not too heavy."
print "He's got %r eyes and %s hair." % (eyes, hair)
print "His teeth are usually %s depending on the coffee." % teeth

# this line is tricky, try to get it exactly right
print "If I add %d, %d, and %d I get %d." % (
    age, height, weight, age + height + weight)


#One site for output: http://docs.python.org/2/tutorial/inputoutput.html
# Better Site for print formatters: http://docs.python.org/release/2.5.2/lib/typesseq-strings.html
# BEst: http://docs.python.org/2/library/stdtypes.html#string-formatting

# %r will print escapes :D


print "Converting: ",inches," to cm:"
cm = (2.54 * inches)
print inches," inches are ",cm," centimeters..."

lbs = (2.20462 * kilos)
print kilos," kilos == ", lbs," pounds"
