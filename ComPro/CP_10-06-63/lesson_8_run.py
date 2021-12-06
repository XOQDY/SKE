import lesson_8

fin = open("words.txt")
word_list = []
for line in fin:
    word = line.strip()
    word_list.append(word)
fin.close()

for word in word_list:
    pass
