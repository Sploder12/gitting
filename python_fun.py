print("hello")
print("Anotha one")
print("Hello Trevor!")
print("I broke it!")

x = 20
if(x == 20):
	print("X was 20!")
	x = 4000
	print("X is now 4000!")
if(x == 0):
	print("9+10=21!")

def wordcount(sentence):
  word = sentence.split()
  print(len(word))

wordcount("this is a sentence")