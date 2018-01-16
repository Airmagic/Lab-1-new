#found python code help from stackoverflow
#Showing the name of the program
print('Camel Casing a sentence')

# getting the sentence from user
sentence = input('Write a short sentence to camelCase :')

# converting the sentence all into lowercase
lowercase = sentence.lower()

# making all the first letter of word uppercase
sentenceTitle = lowercase.title()

# removing all the single spaces from the string
sentenceRemoveSpace = sentenceTitle.replace(' ', '')

# taking the first letter and making a lowercase varible of it
firstLetterLower = sentenceRemoveSpace[0].lower()

# removing the first letter from the sentence
sentenceNoFirstLetter = sentenceRemoveSpace[1:]

# adding the first letter to the sentence
camelCase = firstLetterLower + sentenceNoFirstLetter

# printing out the result in camelCase
print(camelCase)
