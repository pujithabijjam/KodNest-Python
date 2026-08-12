n = int(input())
word_frequency = {}
for i in range(n):
    word = input()
    if word in word_frequency:
        word_frequency[word] += 1
    else:
        word_frequency[word] = 1
for word in word_frequency:
    print(word, word_frequency[word])