# try:
#     A = int(input("enter the Num: "))
#     print(A)

# # except Exception as A:
# #     print(A)
# except ValueError as D:
#     print(D)

###############
#Raise ERoor

# A = int(input("Enter The NUm: "))
# B  = int(input("Enter The NUm: "))

# if (B == 0):
#     raise ZeroDivisionError("LOlee")
# else:
#     print("The Divison of",A, "&", B, "is", A/B)

Age = int(input("Enter Your Age: "))
if(Age < 0 ):
      raise ValueError("Plese Enter Your Age")
elif(Age>18):
    print("Your age is", Age, "you Are eliible For Voting")
else:
    print("Your age is", Age, "you Are Not eliible For Voting")