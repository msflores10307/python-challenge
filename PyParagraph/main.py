import os 
import re

# * Import a text file filled with a paragraph of your choosing. This can be done on either sample file.
filepath = os.path.join(".","Resources","raw_data","paragraph_1.txt")

#initiates important variables
word_len = []
sentence_len = []

#sets file path and reads file
txt = open(filepath)
paragraph = txt.read()

#creates arrays for words and sentences. Removes characters like '.' or "" that mess up the split.
words = paragraph.replace('.','').split(' ')
sentences = re.split("(?<=[.!?\n]) +", paragraph.replace('\n',' ').replace('"',''))

#creates array of word lengths.
for i in range(len(words)):
    word_len.append(len(words[i])) 

#creates array of sentence lengths
for j in range(len(sentences)):
    sentence_len.append(len(sentences[j].split()))

#   * Approximate word count
word_count = len(words)
#   * Approximate sentence count. This is approximate. In the event a name has a period in it like "P.T. Barnum", 
#    it will split the sentence at that point. 
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

#defines path of output file
write_path = os.path.join(".","analysis","analysis.txt")

with open(write_path,"w") as writer_file:
    writer_file.write(output_string) 