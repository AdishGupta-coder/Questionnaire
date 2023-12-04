print("Hello World!!!")
print("Please give one word answer for the following question and for the next question pls type only the flavour.")
icecream = input("What is your favourite flavour of icecream? \n")
name = input("What is your name? \n")
print("Do you know Adish Gupta liked chocolate flavour icecream? \n")
print("Please enter 1 for yes and 2 for no in the following question")
answer = input("Do you like chocolate? \n")
if answer == "1":
    print("So, ",name," likes",icecream," flavour icecream and also likes chocolate.")

elif answer == "2":
    print("So, ",name," likes",icecream," flavour icecream but does not like chocolate.")

else:
    print("Invalid Input")
