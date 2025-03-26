#Set {}
#Dict

"""the set is collection og Non-Repetitve elements.
it is identitfy by {}  
is store only the Unique value. and NO Duplicates is allowed.
Set is the unorded.it means we can NOT performs the idexing and slicing.
Set is the inmutable and mutebale also.
it is hetrogeneous Data types, (We can store multiple data type.) """

s1 ={1,1,2,2,3,3,4,4,5,5,6,7}
# print(type(s1))
# print(s1) #NO duplicates is allowed. 5 will print only once
s1.add(100) #adding element in the last.
# s1.add(34)
# s1.add(384)
# s1.add(344)
# s1.add(324)
# print(s1)

#REMOVE
S2 = {1,2,3,4,5}
# S2.remove(1) #REMOVED the element in te set
# S2.discard(5) #यामध्ये ती value  असो वा  नसो error येणार नाही.

#pop()
# S2.pop() #randomlly removed any element

#clear()
# S2.clear() #clear/empty the set.
# print(S2)



#Dict
"""Dict Identify by {}
    Dict is a set of KeyL Value pair.
    is is Unorded, (B.coz of No index value asosciated with it.)
    Key is Unique and Value Can be repeated."""
    
A = {
    "Rupesh" : "Desai",
    "om" : "D",
    "S" : "M",
    "Rupesh" : "DD"
}
# print(type(A)) #Dict
# print(A)
# print(A['Rupesh']) #desai

B = {
    "Roll Num" : 12,
    "Name" : "ABC",
    "Sub" : 'English'
}

# B.update({"Name": "Rupes"}) #अपडेट करेल abc to  RUpes. Dict  मधील Value  बडल्यानसाठी हिसतरीकक ओन्ली 
# print(B.keys()) # gives ओन्ली keys name 
print(B.get("Roll Num")) #it give the specific data`s key value.



