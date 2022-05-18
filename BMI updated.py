#Body Mass Index 2.0 written by Dominique Hill

#Get Text information from User
name=input("Enter your name")

#Get numeric information from user
height=eval(input("Please Enter height"))
weight=eval(input ("Please Enter weight"))

#Calculate bmi
bmi=weight/height/height*703

#Display Answer
print("Hello",name, "Your bmi is", bmi)

