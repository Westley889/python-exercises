import sys

def find_doups(sentence):
    for word in sentence:
        letters = {''}
        for letter in word:
            if letter not in letters:
                letters.add(letter)
            else:
                return False
    return True
    
sent = []
for words in sys.argv:
    sent.append(words)
sent.remove(sent[0])

print(find_doups(sent))