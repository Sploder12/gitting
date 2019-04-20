def evenodd(number):
	if number%2==0:
		print("Probably even.")
	else:
		print("Maybe Odd.")

def wordcount(sentence):
  word = sentence.split()
  print(len(word))

wordcount("this is a sentence")

evenodd(5)
