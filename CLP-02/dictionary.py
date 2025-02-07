text = "hello this is mostakem mia giving you hello";
words = text.split();
word_count_dictionary = {};

for word in words:
    if word in word_count_dictionary:
        word_count_dictionary[word] =  word_count_dictionary[word] + 1;
    else:
        word_count_dictionary[word] = 1;

print(word_count_dictionary);
