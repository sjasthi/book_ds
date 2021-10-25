'''
Explorations in data science (Level 2 Project for Alex)
=======================================================

Please visit  https://www.gutenberg.org/ and download a book (in text format) that you like.

And you will write a python program to answer these 10 questions.

Your python program should display these 10 choices to the user.
One the user selects a choice, your program produces the answer.


You will be exploring many topics (basic python, conditions, methods, lists, sets, dictionaries, file reading) while doing this project.
Please ensure that your program is well documented, and is thoroughly tested.

[1] What are the top 10 most frequent words in the book?
You should only list top 10 words.
And these words should be alphabetically sorted.

[2] How manys sentences are there in the book?

[3] Provide a table of "sentence number" and the "count of words" in that sentence?

[4] How many words there in Nth sentence?

[5] What is the total number of words in the book?

[6] How many unique words are there in the book?

[7] What is the average number of words per sentence in the book?

[8] Can you produce another book with each word of the book reversed?
Save that book as "reversed.book"

[9] Are there any palindromes in the book?
Ignore the punctuation marks and symbols while figuring out whether a word is a palindrome are not.

[10] Given a word, list all the sentences in which the word is appearing?

'''



'''

Development Strategy: 

Start small with a text file which is very small. 
Once our process is proven/tested, then you can test the same on the big book.

 =================== 5. What is the total number of words in the book? ================

 read the file
 how to read the entire content of the book into a word list
 create a word list
 
 We can answer question 5
 print(" 5. The total number of words in the book are: ")
 
=================== 6. How many unique words are there in the book?   ================

 Convert the above list into a set.
 THen we get the unique set of words.
 Count the length set.
 We can answer question 6
 print(" 6. The total number of unique words in the book are: ")
 
 =================== [1] What are the top 10 most frequent words in the book?   ================

word_dict = { }  // create an empty dictionary
We already have list of words (from question 5)
Loop through each word in the list:
    if word exists in word_dict:
        // bump up the count/ value by 1
    else: // if the word doesn't exist in the word_dict:
        // add new key (word) to the dictionary and set the value as 1
        
Once we come out the loop, we will have a word_dict with "word" as the key and "count" as the value

We can now answer question 1
We just have to sort the dictionary and get the top 10 KEYS
print(" [1] What are the top 10 most frequent words in the book? ")
'''

