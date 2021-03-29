
fruits=["apaple","banana","cherrry"]
print(fruits)
print(fruits[1])

list2=[1,2,3,4,["apple","orange"],[True,False]]
print(list2)
print(list2[1])
print(list2 [2])
print(list2[3:5])

fruits = ["apple","banana","cherry"]
if "apple" in fruits:
    print("yes,'apple' is in the fruits list")
fruits=["apple","banana","cherry","orange","kiwi","mango"]
fruits[1] = "blackcurrant" #change the second item
print(fruits)
fruits[1:3]=["watermelon"]#change the second and third value by replacing it with one value
print(fruits)
fruits.insert(2,"passion") #insert() method inserts item at the specified index
print(fruits)


fruits=["apaple","banana","cherrry"]
fruits.append("orange")
print(fruits)
fruits.append("passion")
#loop through a list
fruits=["apaple","banana","cherrry"]
for x in fruits:
    print(x)
#use the range() and len() functions to create a suitable iterable
for i in range (len(fruits)):
    print(fruits[i])