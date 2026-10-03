import math
word ='When nobody is around, the trees gossip about the people who have walked under them.'
new_sentance="".join(char for char in word if char.isalpha()).lower()
b=math.ceil(math.sqrt(len(new_sentance)))
a=math.ceil(len(new_sentance)/b)
chunks=[new_sentance[i:i+b] for i in range(0,len(new_sentance),b)]
if len(chunks[-1])!=b:
    chunks[-1]=chunks[-1]+" "*(b-len(chunks[-1]))
encoded=[]
for j in range(b):
    new_word=""
    for i in range(a):
        new_word+=chunks[i][j]
    encoded.append(new_word)
output=" ".join(encoded)
print(chunks)
print(new_word)
print(output)