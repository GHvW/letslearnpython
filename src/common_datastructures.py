

# tuple - immutable
stuff = ("hello world!", 42, 99.9)

# list
one_to_five = [1, 6, 2, 2, 3, 4, 5, 9, 1]

# set
suit = {"diamond", "heart", "club", "spade", "spade"}
names = {"Garrett", "Joe", "Bob"}

# not destructive
union = suit.union(names)

print(union)
print(suit)
print(names)

# dictionary
language_creators = { 
    "Python": "Guido van Rossum",
    "C#": "Anders Hejlsberg",
    "F#": "Don Syme",
    "Ruby": "Yukihiro Matsumoto",
    "JavaScript": "Brendan Eich" }

