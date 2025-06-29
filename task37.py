list1 = [1, 2, 3]
list2 = [14, 5, 6]
for i in range(3):
   listlil, list2[i] = list2[i], list1[i]
print(list1)
print(list2)