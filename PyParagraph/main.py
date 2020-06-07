import os 
import re
filepath = os.path.join(".","Resources","raw_data","paragraph_2.txt")

word_len = []
sentence_len = []
txt = open(filepath)
paragraph = txt.read()
words = paragraph.split(' ')
sentences = re.split("(?<=[.!?]) +", paragraph.replace("\n",' '))

for i in range(len(words)):
    word_len.append(len(words[i]))

for j in range(len(sentences)):
    sentence_len.append(len(sentences[j].split()))

print(sentences)
# * Import a text file filled with a paragraph of your choosing.

# * Assess the passage for each of the following:

#   * Approximate word count
word_count = len(words)
#   * Approximate sentence count
sentence_count = len(sentences)
#   * Approximate letter count (per word)
average_word_length = sum(word_len)/len(words)
#   * Average sentence length (in words)
average_sentence_length = sum(sentence_len)/len(sentences)

output_string = f'''
Paragraph Analysis
~~~~~~~~~~~~~~~~~~~~
Approximate Word Count: {word_count}
Approximate Sentence Count: {sentence_count}
Average Letter Count: {average_word_length}
Average Sentence Length: {average_sentence_length}
'''
print(output_string)