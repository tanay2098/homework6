import nltk #importing natural language toolkit
import re   #importing python regular expres
from nltk import tokenize
read_file='content.txt'
write_file='summary.txt'
read_mode='r'
write_mode='w'

total_character_count = 0
total_word_count = 0
total_word_length = 0
total_sentence_length = 0
total_sentence_count = 0
ending_with_ly = []
ten_longest_words = []
ending_with_ly_dictionary = {}

nltk.download("punkt")
content=open(read_file,read_mode,encoding='utf8')
with content:
    data = content.readlines()
    data = [x.strip() for x in data]=
# Dropping all the emtpy elements in the list
    input_lines = [i for i in data if len(i)!= 0]
    for line in input_lines:
        total_character_count += len(line)
    # Removing addition words
        words = [i for i in line.split(" ") if len(i)!= 0]
    # Cleaning up words by removing period, braces, full colon etc
        words = [re.sub(r'[\,\.\"\(\)\!\;\:\?\—]',"", i) for i in words if len(i)!= 0]
        total_word_count += len(words)
    
        for word in words:
            total_word_length += len(word)
            word = word.lower()
            if word.endswith("ly"):
                ending_with_ly.append(word)
    
    # Breaking up senstences require complicated rules to be applied to using a package to do the same
        sentences = tokenize.sent_tokenize(line)
        total_sentence_count += len(sentences)
        for sentence in sentences:
            total_sentence_length += len(sentence)

        ten_longest_words.extend(words)
        ten_longest_words.sort(key=len, reverse=True)
        ten_longest_words = ten_longest_words[:10]


    for word in set(ending_with_ly):
        no_words = ending_with_ly.count(word)
        ending_with_ly_dictionary[word] = no_words
    
    summary=open(write_file,write_mode)
with summary:
    summary.write("Total word count: "+str(total_word_count)+"\n")
    #Total character count:
    summary.write("Total character count: "+str(total_character_count)+"\n")
    #The average word length:
    summary.write("The average word length: "+str(round(1.0*total_word_length/total_word_count, 2))+"\n")    
    #The average sentence length:
    summary.write("The average sentence length: "+str(round(1.0*total_sentence_length/total_sentence_count, 2))+"\n")
    summary.write("\n")
    
    #A word distribution of all words ending in “ly”
    summary.write('A word distribution of all words ending in “ly”\n')
    for word in ending_with_ly_dictionary.keys():
        word_freq = ending_with_ly_dictionary[word]
        summary.write(word+": "+str(word_freq)+"\n")
    summary.write("\n")

    #A list of top 10 longest words in descending order:
    summary.write("A list of top 10 longest words in descending order:\n")
    summary.write(", ".join(ten_longest_words))