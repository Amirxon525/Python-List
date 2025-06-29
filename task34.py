nums = [1, 2, 3, 7, 8, 9]
result = []
i = 0
while i < len (nums):
 j = i + 1
while j < len (nums) :
    if nums [i] + nums [j] == 10:
     result. append ([nums [i], nums [j]])
j += 1
i += 1
print (result)