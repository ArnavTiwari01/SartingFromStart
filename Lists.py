# Basic Lists

list1 = ["Mango", "Orranges", "Apple"]
print(list1)

# Access list items 

list2 = ["Cherry", "Watermelon", "strawberry"]
print(list2[1])         # values can be added negative too


# Range of indexes

list3 = ["cherry", "bananana", "cheeta", "lion"]   
print(list3[1:3])           # it will print bananana, cheeta and lion
                            # these values will be negative too like [-1:-5]

# to check the items in a list

list4 = ["Arnav", "ritivk", "mridul"]

if "mridul" in list4:
    print("yes he is in the list")          #   "yes he is in the list"

else:
    print("no he is not in this list")

# Changing list items value

mylist = ["CAR", "BUS", "SCHOOL", "FEMALES"]

mylist[1] = "Cheetah"
print(mylist)                                # it would replace bus and add cheetah 

# changing multple values in the list 

mylistmain = ["ARNAV", "MRIDUL", "GATIK", "SUHAVI"]

mylistmain[1:3] = "MIA"
print(mylistmain)                             # it would replace the 2 -> 3 objects and add "Mia"!


# using insert to add iteams without replacing them 

mylist2 = ["hello", "hey", "slay"]

mylist2.insert(2, "cheetah")                    # after hey there will be cheetah term added in the list
print(mylist2)


# Append iteams, to add an item at the end of the list 

mylisty = ["APPLE", "BANANA", "CHERRY", "TREE"]

mylisty.append("Hello")
print(mylisty)                                  # At the end of the list it would add 'Hello'!

# inster, could be used to inster at a particular position

mylistylist = ["cheeta", "tiger", "lion"]

mylistylist.insert(1, "MURGA")
print(mylistylist)                               # it would replace tiger and put murga



# we can use extend to merge 2 lists

transformer = ["KAWE", "GFGDFSD", 'SDDSDS']
trans2 = ["eref", "erere", "dfasdf"]

transformer.extend(trans2)
print(transformer)                              # we basically added all the elements in trans2 to transformer


# remmove, to remove an item from the list
kys = ["hello", "ji", "wsup"]
kys.remove("ji")                # remove ji

kys.insert(1,"randi")
print(kys)                      # add randi making it informal 


# POP, does the same thing

tralala = ["ARNAV","SUHAVI","GATIK"]
tralala.pop[1]

print(tralala)          #suhavi will be eliminated '


okok = ["hello", "sir"]

okok.pop()
print(okok)                     # it would remove the last element of the list

# del and clear, which will also do the same thing

gg = ["bonnie", "ebony", "teacher"]
del gg[1]

print(gg)                   # ebony would be removed 

                            # if we wont write anything in square brackets the whole list will be removed.


# loop lists

tity = ["apple", "banana", "cherry"]

for x in tity:
    print(x)                        # it would pring down all the list items 


tiy = ["car", "bus", "recatangle"]

for x in range(len(tiy)):
    print(x)                        # breakdown all the elements


jagran = ["apple", "banana", "cherry"]


# while, going through all index numbers

listop = ["apple", "banana", "cheetah"]

i = 0
while i < len(listop):
    print(listop[i])
    i = i + 1


# for loop, doing the same

twin = ["apple", "banana", "chocolate"]

for x in twin:
    print(x)                # print all elements in x


# list comprehension

fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist =  []

for x in fruits:
    if "a" in x:
        newlist.append(x)

print(newlist)                 # it would print all the elements with a in it   


fruits = ["apple", "banana", "cherry", "kiwi", "mango"]

newlist = [x for x in fruits if "a" in x]

print(newlist)


# sorting the lists

list09 = ["banana", "Orange", "Kiwi", "cherry"]
list09.sort()

print(list09)               # it would sort the list in alphabetical order

# numerical sorting
thislist = [100, 50, 65, 82, 23]
thislist.sort()
print(thislist)          # it would sort the list in ascending order

# reverse sorting alphabetically

thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort(reverse = True)
print(thislist)          # it would sort the list in descending order

# reverse sorting numerically

thislist = [100, 50, 65, 82, 23]
thislist.sort(reverse = True)
print(thislist)         # it would sort the list in descending order

# case insensitive sorting
thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.sort()
print(thislist)         # it would sort the list in case sensitive manner

# case insensitive sorting
thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.sort(key = str.lower)
print(thislist)     # it would sort the list in case insensitive manner

# COPY LISTING (list and copy)

thislist = ["apple", "banana", "cherry"]
mylist = thislist.copy()
print(mylist)        # it would copy the list to mylist 


# Join lists

list1 = ["a", "b", "c"]
list2 = [1, 2, 3]

list3 = list1 + list2
print(list3)    # it would join both the lists

# append listing using for 

list1 = ["a", "b" , "c"]
list2 = [1, 2, 3]

for x in list2:
  list1.append(x)

print(list1)  # it would append list2 to list1
# using extend to join 2 lists  

