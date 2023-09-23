# python-for-everyone-exercise
"Python_for_Everyone" course exercises

## Chapter 5 Iteration
- Write a program which repeatedly reads numbers until the user enters “done”. Once “done” is entered, print out the total, count, and average of the numbers. If the user enters anything other than a number, detect their mistake using try and except and print an error message and skip to the next number.
- print smallest and largest number

## Chapter 6 Strings
- Exercise 1: Write a while loop that starts at the last character in the string and works its way backwards to the first character in the string, printing each letter on a separate line, except backwards.
- Exercise 3: Encapsulate this code in a function named count, and gen- eralize it so that it accepts the string and the letter as arguments.
- Exercise 5: Take the following Python code that stores a string:
str = 'X-DSPAM-Confidence:0.8475'
Use find and string slicing to extract the portion of the string after the colon character and then use the float function to convert the extracted string into a floating point number.

## Chapter 7 Files
- Exercise 1: Write a program to read through a file and print the contents of the file (line by line) all in upper case.
- Exercise 2: Write a program to prompt for a file name, and then read through the file and look for lines of the form: X-DSPAM-Confidence(Test your file on the mbox.txt and mbox-short.txt files.)
- Exercise 3: Sometimes when programmers get bored or want to have a bit of fun, they add a harmless Easter Egg to their program Modify the program that prompts the user for the file name so that it prints a funny message when the user types in the exact file name “na na boo boo”. The program should behave normally for all other files which exist and don’t exist.

## Chapter 8 Lists
- Exercise 1: Write a function called chop that takes a list and modifies it, removing the first and last elements, and returns None. Then write a function called middle that takes a list and returns a new list that contains all but the first and last elements.
- Exercise 2&3: Rewrite the guardian code
- Exercise 4: Write a program to open the file romeo.txt and read it line by line. For each line, split the line into a list of words using the split function. For each word, check to see if the word is already in a list. If the word is not in the list, add it to the list. When the program completes, sort and print the resulting words in alphabetical order.
- Exercise 5: Write a program to read through the mail box data and when you find line that starts with “From”, you will split the line into words using the split function. You will parse the From line and print out the second word for each From line, then you will also count the number of From (not From:) lines and print out a count at the end.
- Exercise 6: Rewrite the program that prompts the user for a list of numbers and prints out the maximum and minimum of the numbers at the end when the user enters “done”. Write the program to store the numbers the user enters in a list and use the max() and min() functions to compute the maximum and minimum numbers after the loop completes.
