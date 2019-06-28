''''
Exercise 6 (and Solution)
Ask the user for a string and print out whether this string is a palindrome or not. (A palindrome is a string that reads the same forwards and backwards.)

Discussion
Concepts for this week:

List indexing
Strings are lists
'''
'''''
wrd=input("Please enter a word")
wrd=str(wrd)
rvs=wrd[::-1]
print(rvs)
if wrd == rvs:
    print("This word is a palindrome")
else:
    print("This word is not a palindrome")
 ''''   
a=str(input("Enter a string:"))
x=int(len(a))
print(x)
b=[i for i in a]
print(b[::-1])