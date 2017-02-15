# initializing formatter to be equal to 4 raw format placeholders
formatter = "%r %r %r %r"

# printing variable formatter replacing the 4 raw formatters with 1, 2, 3, 4
print formatter % (1, 2, 3, 4)
# printing variable formatter replacing %r with "one", "two" etc.
print formatter % ("one", "two", "three", "four")
# printing formatter replacing %r with booleans True/False
print formatter % (True, False, False, True)
# printing formatter showing the %r four times
print formatter % (formatter, formatter, formatter, formatter)
# print formatter shows four strings in place of %r
print formatter % (
    "I had this thing.",
    "That you could type up right.",
    "But it didn't sing.",
    "So I said goodnight."
)
