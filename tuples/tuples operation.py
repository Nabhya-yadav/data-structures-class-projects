# Write a program to perform the follow operations

# 1. Create a tuple with differen datatypes
differenttuple=(1,2,3,"string",20.20,True)
print(differenttuple)

# 2. Create another tuple of integers
numbertuple=(99,76,86,11,23,43,58,15)
print(numbertuple)

# 3. Create a new tuple by adding 9 to the previous tuple
numbertuple=numbertuple+(9,)
print(numbertuple)

# 4. Count the occurrence of an elements in the tuple
repeatingtuple=(1,1,2,3,4,4,6,6,7,8,9,0,0)
print(repeatingtuple.count(0))

# 5. Perform slicing on tuple
slice=numbertuple[2:7]
print(slice)