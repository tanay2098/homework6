import string #import string module
read_file = "book.txt"
write_file = "summary_book.txt"
read_mode = 'r'
write_mode = 'w'

book = open(read_file, read_mode)# opening read file
with book:
    data = book.read().upper()# converting the read data into upper case.
character_dictionary = {} #initializing a dictionary to store characters
for char in data:
    if char.isalpha(): #check if the data is alphabet only.
        character_dictionary[char] = data.count(char)# assigning the count of characters to dictionary
  
summary = open(write_file, write_mode)#opening the write file
with summary:
    for letter in sorted(character_dictionary.keys()): #sort the dictionary
        summary.write(f'{letter} {character_dictionary[letter]}\n')
    if len(character_dictionary) == 26:#if all 26 alphabets are there
         summary.write("\nIt has all letters.")
    else:
         summary.write("\nIt doesn't have all letters.")