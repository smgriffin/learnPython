name = 'Zed A. Shaw'
age = 35  # not a lie
height = 74  # inches
weight = 180  # lbs
eyes = 'Blue'
teeth = 'White'
hair = 'Brown'


print "Let's talk about %s." % name
print "He's %d inches tall.  That's %f centimeters" % (height, height * 0.393701)
print "He's %d pounds heavy.  That's %f kiligrams." % (weight, weight * 0.6)
print "Actually that's not too heavy."
print "He's got %s eyes and %s hair." % (eyes, hair)
print "His teeth are usually %s depending on the coffee." % teeth

# this line is tricky, try to get it exactly right
print "If I add %d, %d, and %d I get %d." % (
    age, height, weight, age + weight + weight)  # 35 + 74 + 180 = 289