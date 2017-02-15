# Here's some new strange stuff, remember type it exactly.

# Sets days equal to string listing days separated by spaces
days = "Mon Tue Wed Thur Fri Sat Sun"
# Sets variable months equal to months separated by newlines
months = "Jan\nFeb\nMar\nApr\nMay\nJun\nJul\nAug"

# Print string followed by string from days variable
print "Here are the days: ", days
# Print string followed by string from months label
print "Here are the months: %r" % months

# Tripleq quotes allows you to write a string across multiple lines
print """
There's something going on here.
With the three double quotes.
We'll be able to type as much as we like.
Even 4 lines if we want, or 5, or 6.
"""
