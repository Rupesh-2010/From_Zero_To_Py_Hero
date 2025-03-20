# def readFile(filename):
#     with open(filename, "r") as f:
#         print(f.read())

# readFile("file.txt")

###########################

# num = int(input("Enter Your Num: "))

# table = [num*A for A in range(1,11)]
# print(table)

########################3


# A = int(input("Enter Your Num: "))
# B = int(input("Enter Your Num: "))
#     # C = A/B

# try:
#     print(A/B)
# except:
#     print("INfinit")

#################3

num = int(input("Enter Your Num: "))

table = [num*A for A in range(1,11)]

print(table)


with open("file.txt","a") as Rup:
    Rup.write(str(table))
