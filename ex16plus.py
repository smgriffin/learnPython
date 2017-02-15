from sys import argv

script, filename = argv

rText = open(filename)
print rText.read()
