words = ["kitob", "dastur", "AI", "hello", "python", "programming"]
longest_word = None
for word in words:
 if longest_word == None:
  longest_word = word
 elif len(word) > len (longest_word) :
  longest_word = word
print (longest_word)