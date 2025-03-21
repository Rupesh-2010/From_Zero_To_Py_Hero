#List []
""" List is the container that store all types of elements, i.g.. str, int, bool,float.(it is the hetrogeneous data type.)
a list is a Flexibale, muteable it means it can be changebele and accept the duplicate values.
you can modify the list, by append(), remove(), and sort() or pop()
duplicates are not allowed. """



A = [1,2,3,4,5,6,7,8,9,100,100,100,100]
# print(A[1:7])

print(type(A))


L1 = ["R", "U", "P", "E", "S", "H"]
# L1[0] = "Z" #it change the R to Z

L1[0:3] = "Z", "Z", "Z"
# print(L1)


A = [1,2,3,4,5,6,7,8,9,100]
B = [9,9,9,9,9,9,9,9]
# A.append(2222) #add to the end of the list
# A.insert(0,11111) #first is Index number and secod is th New element that iwant to change at the index num 1
# A.extend(B)
A.reverse()

print(A)

