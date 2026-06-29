# 1. Write a program to create a dictionary of Hindi words with values as their English
# translation. Provide user with an option to look it up!

d={
"good":"accha",
"cat":"billi", 
"bittergaurd":"karela",
"lauki":"bottlegaurd",
"chair":"kursi",


}

word=(input("enter the word to know the meaning:"))

print(d.get(word))