#tuple
thistuple = ("apple", "banana", "cherry")
print(thistuple)
print(len(thistuple))
thistuple = ("apple",)
print(type(thistuple))
thistuple = ("apple")
print(type(thistuple))

#Set
thisset = {"apple", "banana", "cherry"}
print(thisset)
thisset = {"apple", "banana", "cherry", "apple"}
print(thisset)
print(len(thisset))
print(type(thisset))


#Dictionaries
y = {}
x = {1: "one", 2: "two", 3: "three"}
y['one'] = 1
y['two'] = 2
print(y)
y['two'] = 'dos'
print(y)
del y['two']
print(y)
print(len(y))