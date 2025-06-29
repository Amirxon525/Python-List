
nums = []
for i in range (10):
       num = int (input (f"{i + 1}-son = "))

nums. append (num)
result = []
for num in nums:
   if nums. count (num) == 1:
        result. append (num)
print (result)