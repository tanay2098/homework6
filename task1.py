import os
import sys
import string

#read mode variables
READ_FILENAME = 'content.txt'
READ_MODE = 'r'

#write mode variables
WRITE_FILENAME = 'summary.txt'
WRITE_MODE = 'w'

#variable declaration
line_count = 0
word_count = 0
char_count = 0
sentence_count = 0

#dictionary declaration
ly_ending_dict = {} #dictionary for ly ending words
long_word_dict = {} #dictionary for longest word
ten_long_word_dict = {} #dictionary for top 10 longest words

#process file data in the try block
article_file = open(READ_FILENAME, READ_MODE,encoding='utf8') #opening read file
summary_file = open(WRITE_FILENAME, WRITE_MODE) #opening write file

with article_file,summary_file: #automically closes files
    for line in article_file:
            #for removing blank lines
        if len(line.split()) == 0:
            continue

            #total sentence count before removing punctuation marks from read line
        sentence = line.split('.\n:')
        sentence_count += len(sentence)

            #operations on read lines
        line = line.lower() #changing to lower for frequency
        line = line.translate(line.maketrans("", "", string.punctuation)) #removing punctuation
        line = line.replace("—",'') #hyphen npt removed with above code, so replacing hyphen

            #counter for line count
        line_count += 1

            #total word count
        words = line.split()
        word_count += len(words)

            #total character count
        char_count += sum(len(char) for char in words)

            #set longest word
        max_len = len(max(words, key=len))

            #words ending in ly
            #longest words
        for ly_word in line.split():
                # logic for longest words
            if len(ly_word) == max_len:
                if ly_word not in long_word_dict:
                    long_word_dict[ly_word] = len(ly_word)

                #logic for words ending in ly
            if ly_word.endswith('ly'):
                if ly_word in ly_ending_dict:
                    ly_ending_dict[ly_word] += 1
                else:
                    ly_ending_dict[ly_word] = 1

        #write data to summary.txt
    summary_file.write(f'Total word count: {word_count}\n')
    summary_file.write(f'Total character count: {char_count}\n')
    summary_file.write(f'The average word length: {(char_count/word_count):.2f}\n')
    summary_file.write(f'The average sentence length: {(word_count/sentence_count):.2f}\n')
    summary_file.write('\n')

        #write ly ending words
    summary_file.write('A word distribution of all words ending in “ly”\n')
    for ly_e_word,count in sorted(ly_ending_dict.items()):   
        summary_file.write(f'{ly_e_word}: {count}\n')
    summary_file.write('\n')
        
        #write longest words
    summary_file.write('A list of top 10 longest words in descending order:\n') 
    ten_long_word_dict = {long_word: count for long_word,count in sorted(long_word_dict.items(),key = lambda x: x[1],reverse = True)}
    for longest_words in sorted(list(ten_long_word_dict)[0:10],reverse = True): 
        summary_file.write(f'{longest_words}, ')