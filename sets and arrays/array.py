import array as arr

a = arr.array('i', [1,2,3,2,4, 4,5])

for i in range(0, len(a)):

    print(a[i], end=" ")


a.insert(5, 6)

print(a)

print(a[2])

a.remove(2)

print(a)

count = a.count(4)

print(count)

rev = a.reverse()

print(*a)