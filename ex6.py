x = "There are %d types of people." % 10  # assigning variable x with a string.
                                          # %d leaves a space for # variable which is 10
binary = "binary"  # set binary equal to string "binary"
do_not = "don't"  # set do_not equal to string "don't"
y = "Those who know %s and those who %s." % (binary, do_not)  # sets y equal to string with two 
                                                              # spaces for strings to be formatted in
                                                              # these strings are filled with variables
                                                              # binary and do_not

print x  # printing variable x
print y  # printing variable y

print "I said %r." % x  # printing the string with %r (raw formatting) which shows the string x with python formatting
print "I also said: '%s'." % y  # prints the string with %s which prints variable y with string formatting

hilarious = False  # initializes variable hilarious as boolean False
joke_evaluation = "Isn't that joke so funny?! %r"  #sets joke_evaluation equal to a string with a raw format %r at end

print joke_evaluation % hilarious  # prints variable joke_evaluation replacing the %r with variable hilarious

w = "This is the left side of..."
e = "a string with a right side."

print w + e  # concecating strings w + e which are set above

# Places where a string is put inside a string line 2x 5, 14, 13
