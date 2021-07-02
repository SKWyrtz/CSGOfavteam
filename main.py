import itertools

text_file = open("teams.txt",  "r")
lines = text_file.read()
lines = lines.splitlines()
print(lines)
#https://stackoverflow.com/questions/16603282/how-to-compare-each-item-in-a-list-with-the-rest-only-once
