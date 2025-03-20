# Q1
# A1 = int(input("Enter the Num1: "))
# A2 = int(input("Enter the Num2: "))
# A3 = int(input("Enter the Num3: "))
# A4 = int(input("Enter the Num4: "))

# if(A1>A2 and A1>A3 and A1>A4):
#     print(A1, "is the Greast Number.")
# elif(A2>A1 and A2>A3 and A2>A4):
#     print(A2, "is Greast Number.")
# elif(A3>A1 and A3>A2 and A3>A4):
#     print(A3, "is Greast Number.")
# else:
#     print(A4,"is Greast Number.")


# #Q2

# Sub1 = int(input("Enter Sub 1 Marks: "))
# Sub2 = int(input("Enter Sub 2 Marks: "))
# Sub3 = int(input("Enter Sub 3 Marks: "))

# Total = (Sub1+Sub2+Sub3)/300
# print("Your Score is: ", Total)
# if(Total<=33):
#     print("You are fail.")
# else:
#     print("You are Pass")

# Q3
# A =[1,2,3,4,5,"R"]
# print("r" in A)

# Q4
# Username= input("enter Your Username: ")
# if(len(Username)<=10):
#     print("Under the 10 charactor")
# else:
#     print("More than 10 charactor")

# Q5
# List= ["Rupesh","Vishal","Sonya","Mayur","Anjali"]
# A = input("enter the name: ")
# print(A in List)

# Q6

Marks= int(input("Enter Your Marks: "))
if(Marks>=90):
    print("Your Marks is", Marks,"You get Ex grade")
elif(Marks>=80):
    print("Your Marks is", Marks,"You get A grade")
elif(Marks>=70):
    print("Your Marks is", Marks,"You get B grade")
elif(Marks>=60):
    print("Your Marks is", Marks,"You get C grade")
elif(Marks>=50):
    print("Your Marks is", Marks,"You get D grade")
else:
    print("Your Marks is", Marks, "it is Bellow 50%, You are fail. ")