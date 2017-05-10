from collections import Counter
def word_Count(sentence):
	return Counter(map(str, sentence.split()))

print(word_Count("hello from the outside hello"))