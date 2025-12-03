set1={1,2,3,4,5}
set2={2,3,5,6,8}

set3= set1.union(set2)
print(set3)

set3= set1.intersection(set2)
print(set3)

set3= set1.symmetric_difference(set2)
print(set3)

set1.pop()
print(set1)

set2.add(10)
print(set2)