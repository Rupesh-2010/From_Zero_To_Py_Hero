# Dict
# Q.1
# Words= {
#     "Madat" : "Help",
#     "Raaja" : "King",
#     "shaala" : "school",
#     "Guru" : "teacher",
#     "vishay": "Subject"
# }
# # S = Words.get("Raaja")
# Word= input("Enter the words: ")
# print(Words[Word])

# Q.2
# Num1 = int(input("Enter the Num 1: "))
# Num2 = int(input("Enter the Num 2: "))
# Num3 = int(input("Enter the Num 3: "))
# Num4 = int(input("Enter the Num 4: "))
# Num5 = int(input("Enter the Num 5: "))
# Num6 = int(input("Enter the Num 6: "))
# Num7 = int(input("Enter the Num 7: "))
# Num8 = int(input("Enter the Num 8: "))

# N = {Num1, Num2, Num3, Num4, Num5, Num6, Num7, Num8}
# print(N)
# print(type(N))

#Q3
# S = {18, "18"}
# print(S)
# print(type(S))

#Q4
# S = set()
# S.add(20)
# S.add(20.0)
# S.add('20')
# print(len(S))

#Q5
# A = ()
# print(type(A))
# s = ()
# print(type(s))

#Q6
Dict = { }
A = input("Enter Your Fav lang: ")
Dict.update({"Rohit" : A })
B = input("Enter Your Fav lang: ")
Dict.update({"Sonu" : B })
C = input("Enter Your Fav lang: ")
Dict.update({"Vishal" : C })
D = input("Enter Your Fav lang: ")
Dict.update({"Rupesh" : D })

print(Dict)