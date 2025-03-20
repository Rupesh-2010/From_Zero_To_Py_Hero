# try:
#     A = int(input("Enter the Num: "))
#     C = 1/A
# except Exception as e:
#     print("Exception Pop up..")
#     print("Rupesh")
# print("thans for useing")
# # print(C)




def increment(num):
    try:
        return int(num)+1
    except:
        raise ValueError("This not good")
    
A = increment(99)
print(A)

