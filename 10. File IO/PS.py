# A = open("file.txt")
# word = A.read()
# if("Rupesh" in word):
#     print("The Word Rupesh Present in the the File ")
# else:
#     print("The Word is not found.")
# A.close()

##########################################

score = int(input("Enter Your score: "))
f = open("Hi-score.txt", "w")
f.write(score, 'a')
print(f)
f.close()
