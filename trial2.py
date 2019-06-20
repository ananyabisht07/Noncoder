from collections import Counter
with open('infile.txt','r') as f:
	list1=[word for line in f for word in line.split()]
word_count=Counter(list1)
for word, count in word_count.most_common(5): 
	print('%s:%d' %(word,count))


'''x=sorted(word_count.items(),key=lambda item: item[1])
print(x)
x.reverse()
print(x)'''




