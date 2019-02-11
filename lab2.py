
#Due: February 6th at the beginning of class

#Dominique Mendes

# Each of the sentences below are followed by a set of related instructions.
# After each instruction, add your code that does what's being asked, as well as
# a print statement that shows your work. Don't forget to print new lines as well,
# or your output will be a mess!

import re

solution_separator = "\n\n****************************************\n\n"

# For example:
s0 = "This is a test"
print (s0 + "\n")

print (solution_separator)

# 1) Write a regular expression and if statement that checks if T is the first letter
pattern = re.compile(r"[T]")
if re.search(pattern, s0):
    print ("It starts with 'T'!" + "\n")
else:
    print ("My regex is incorrect, it should detect the 'T'!" + "\n")

print (solution_separator)

# 2) Use a regular expression to decompose the string into words and place those words intp a list.
#    Extract the first word into a variable and print it
words = re.split("\W+", s0)
print (words)
print ("\n")
first_word = words[0]
print ("The first word is: '" + first_word + "'\n")

print (solution_separator)

# 3) Split the sentence into an array of individual words called words and use a for loop to print it.
#    for each var in vars:
#        (your code here)
#
pattern = ''
words = re.split(pattern, s0)
for word in words:
    print (word + "\n")


print (solution_separator)


# 4)
s1 = "Mary was born on September 17, 1986"

# a) Write a regular expression and if statement that checks if the name "Mary" in the sentence.
pattern = re.compile(r"[Mary]")
if re.search(pattern, s1):
    print ("It starts with 'Mary'!" + "\n")
else:
    print ("My regex is incorrect, it should detect 'Mary'!" + "\n")
    
# b) Write a regular expression and if statement that checks if the sentence contains a 4 digit number.
pattern= re.compile(r"[0-9]{4}")
if re.search(pattern, s1):
    print("There is a 4 digit number here")
else:
    print ("My regex is incorrect, it should detect the 4 digit number!" + "\n")
    
# c) Write a regular expression to extract that number into a variable b_year and print it in this sentence:
#    "The person was born in b_year."
pattern= re.compile(r"[0-9]{4}")
year= re.search(pattern, s1)
print("The person was born in "+ year.group() +"\n")

print (solution_separator)
       
# 5)
s2 = "The dog, named Dog, was doggedly trying to dodge the fog."
# a) Write a regular expression to match the word "dog", but not the name "Dog"
pattern= re.compile(r"[dog]")
if re.search(pattern, s2):
    print ("It matches with 'dog'!" + "\n")
else:
    print ("My regex is incorrect, it should detect 'dog'!" + "\n")

# b) Save the output from this match into a list and print the list to verify it is not matching anything else.
words= re.findall(pattern, s2)
for word in words:
    print (word + "\n")

# c) Write a regular expression to match "dog" and "Dog" using a flag (see the cheat sheet).
pattern= re.compile(r"[dog]", re.I)
if re.search(pattern, s2):
    print ("It matches with 'Dog'!" + "\n")
else:
    print ("My regex is incorrect, it should detect 'Dog'!" + "\n")

# d) Write a regular expression to match "dog" or "fog"
pattern= re.compile(r"dog|fog")

# e) Print all outputs.
words= re.findall(pattern, s2)
for word in words:
    print (word + "\n")
print (solution_separator)

# 6)
s3 = "18785 is the 5 digit number I want not 43744, 34553, or 11111"

# a) Write a regular expression to extract the first number (try to do it without using the exact string).
pattern= re.compile(r'[18]{2}[5-9]{3}')
if re.search(pattern, s3):
    print("It worked!\n")
else:
    print("I missed the right number!")
# b) Write a regular expression to extract all numbers, store them in an array, then print the array.
words= re.findall('\d+', s3)
for word in words:
    print (word + "\n")
print (solution_separator)

# 7) Write a regular expression to trim the left and right whitespace and print the trimmed output.
s4 = "    There is preceding white space in this sentence, and whitespace at the end        "
result= re.sub(r"^\s+", "", s4)
print(result)
print (solution_separator)

# 8)
s5 = "junk data penguin begin tennis for 2 end begin Zelda and Link end begin Oculus Rift end no cheating by using " \
     "positional text flags"

# a) Write a regular expression to print everything from the first "begin" to the last "end".
pattern= (r"(begin)(.*)(end)")
result= re.findall(pattern, s5)
print(result)
# b) Write a regular expression to print only the text from the first "begin" to the first "end"
pattern= (r"(begin)(.*?)(end)")
result= re.findall(pattern, s5)
print(result[0])

# c) Write a regular expression to extract all of the text between "begin"s and "end"s into an array.
pattern= (r"(begin)(.*?)(end)")
results= re.findall(pattern, s5)

# d) Print all outputs.
print(results)
print (solution_separator)

# 9)
s6 = "The date 5/17/1982 is trickier to get"

# a) Write a regular expression to extract the date.
pattern= (r"^\d{1,2}/\d{1,2}/\d{4}$")
# b) Capture the date in a variable f_date
date= re.findall(pattern, s6)
print(date)
# c) Split the date and store it as month, day, year
# d) Convert the date to date format year-month-day where month and day always have 2 digits. Save the
#    result in comp_date
# e) Print comp_date

print (solution_separator)

# 10) Extra Credit:
s8 = "These are some dates: 1/23/2011, 2/1/2006, 12/31/2007, 9/15/1993, 04/23/1797."

# a) Use a regex to collect the dates into a list
# b) Use the code above to convert them into yyyy-mm-dd format.
# c) Print the dates in chronological order

print (solution_separator)
