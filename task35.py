
words = ["kitob", "dastur", "AI", "hello", "python", "programming"]
result = [
[], # <=3 harfli
[], # 4-6 harfli
[], # >6 harfli
]
for word in words:
 n = len (word)
if n <= 3:
 result [0]. append (word)
elif n >= 4 and n <= 6:
  result [1]. append (word)
else:
 result [2]. append(word)

print (result)