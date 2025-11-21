numbers=[1,2,3,4,98,68,96,56,86]
null=[]
print(numbers)
for i in numbers:
    print(i)

print(len(numbers))

print(numbers[2])

print(numbers[2:5])

numbers.append(75)
print(numbers)

numbers.remove(96)
print(numbers)

numbers.reverse()
print(numbers)

numbers.sort()
print(numbers)
