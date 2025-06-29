nums = [3, 5, 3, 2, 5, 5, 1, 1, 1,
1, 1, 3, 21]
result = None
for num in nums:
    if result == None:
       result = num
    elif nums. count (num) > nums. count (result):
      result = num
print (result)