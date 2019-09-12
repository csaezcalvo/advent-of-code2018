file = "/home/carlos/advcode2018/input2"
data = open(file,'r')
list_of_words = []
for line in data:
    list_of_words.append(line)

def distance(word1, word2):
    d = 0
    for i in range(len(word1)):
        if word1[i] != word2[i]:
            d +=1
    return d

def correct_boxes(lst):
    for word in lst:
        for word2 in lst:
            if distance(word, word2) == 1:
                return (word, word2)

def common_letters(tuple_of_words):
    word1 = tuple_of_words[0]
    word2 = tuple_of_words[1]
    letters = []
    for i in range(len(word1)):
        if word1[i] == word2[i]:
            letters.append(word1[i])
    return ''.join(letters)

print(correct_boxes(list_of_words))
print(common_letters(correct_boxes(list_of_words)))


