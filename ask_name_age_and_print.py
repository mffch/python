from datetime import date

name =input("Enter your name:")
age=input("How old are you?")
real = 100 - int(age)
year_ = date.today().year 
future = (int(year_) + int(real))


number=input("Enter a number:")
i=1
while i<=int(number):
    print("You will be 100 in " + str(future))
    i+=1