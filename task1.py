import nltk #importing natural language toolkit
import re   #importing python regular expression
from nltk import tokenize #import tokenize from nltk
read_file='content.txt'
write_file='summary.txt'
read_mode='r'
write_mode='w'

#declaring variables
total_character_count = 0
total_word_count = 0
total_word_length = 0
total_sentence_length = 0
total_sentence_count = 0
ending_with_ly = []
ten_longest_words = []
ending_with_ly_dictionary = {} # dictionary to store words ending with ly

nltk.download("punkt")# downloading a sentence tokenizer to divide text into list of sentences
content=open(read_file,read_mode,encoding='utf8')#opening the read file
with content:
    data = content.readlines()
    data = [x.strip() for x in data]
    input_lines = [i for i in data if len(i)!= 0]# removing empty elements from list
    for line in input_lines:
        total_character_count += len(line)
        words = [i for i in line.split(" ") if len(i)!= 0]# Remove additional words    
        words = [re.sub(r'[\,\.\"\(\)\!\;\:\?\—]',"", i) for i in words if len(i)!= 0]# Remove punctuations from content
        total_word_count += len(words)

        for word in words:
            total_word_length += len(word)
            word = word.lower()
            if word.endswith("ly"):# setting the condition for words ending with ly
                ending_with_ly.append(word)
    
        sentences = tokenize.sent_tokenize(line)# Using toeknize to break up text into sentence
        total_sentence_count += len(sentences)
        for sentence in sentences:
            total_sentence_length += len(sentence)

        ten_longest_words.extend(words)
        ten_longest_words.sort(key=len, reverse=True)#sort the 10 longest words in descending order 
        ten_longest_words = ten_longest_words[:10]# store the words in dictionary

    for word in set(ending_with_ly):
        no_words = ending_with_ly.count(word)
        ending_with_ly_dictionary[word] = no_words
    
    summary=open(write_file,write_mode)
with summary:
    summary.write("Total word count: "+str(total_word_count)+"\n")#Total word count
    summary.write("Total character count: "+str(total_character_count)+"\n")#Total character count
    summary.write("The average word length: "+str(round(1.0*total_word_length/total_word_count, 2))+"\n")#average word length:    
    summary.write("The average sentence length: "+str(round(1.0*total_sentence_length/total_sentence_count, 2))+"\n")#The average sentence length:
    summary.write("\n")
    summary.write('A word distribution of all words ending in “ly”\n')
    for word in ending_with_ly_dictionary.keys():
        word_freq = ending_with_ly_dictionary[word]
        summary.write(word+": "+str(word_freq)+"\n")
    summary.write("\n")
    summary.write("A list of top 10 longest words in descending order:\n")
    summary.write(", ".join(ten_longest_words))