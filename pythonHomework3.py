# Exercise 1: Print each item in the list
lst=["koala", "cat", "fox", "panda", "chipmunk", "sloth", "penguin", "dolphin"]
for item in lst:
    print(item)
    
    
# Exercise 2: Write a for loop which print "Hello!, " plus each name in the list. i.e.: "Hello!, Sam"

lst=["Sam", "Lisa", "Micha", "Dave", "Wyatt", "Emma", "Sage"]
for item in lst:
    print("Hello! "+item)
    

# Exercise 3: Write a for loop that iterates through a string and prints every letter
str="Antarctica"
for letter in str:
    print(letter)
    
    
# Exercise 4: Type a code inside the for loop so that counter variable named c is increased by one each time loop iterates
str = "Civilization"

c = 0
for i in str:
    c += 1
    print(c)
    
    
# Exercise 5: Using a for loop and .append() method append each item with a Dr. prefix to the lst
lst1=["Phil", "Oz", "Seuss", "Dre"]
lst2=[]
for item in lst1:
    lst2.append("Dr "+item)
print(lst2)

# Exercise 6: Write a for loop which appends the square of each number to the new list
lst1=[3, 7, 6, 8, 9, 11, 15, 25]
lst2=[]

for i in lst1:
    i *= i
    lst2.append(i)

print(lst2)

# Exercise 7: Write a for loop using an if statement, that appends each number to the new list if it's positive
lst1=[111, 32, -9, -45, -17, 9, 85, -10]
lst2=[]

for i in lst1:
    if i >= 0:
        lst2.append(i)

print(lst2)

# Exercise 8: Using for loop and if statement, append the value minus 1000 for each key to the new list if the value is above 1000
dict={"z1":900, "t1": 1100, "p1": 2300, "r1": 1050, "k1": 3200, "g1": 400}
lst=[]

for i in dict:
    if dict[i] > 1000:
        lst.append(dict[i]-1000)

print(lst)

# Exercise 9: Write a for loop which appends the type of each element in the first list to the second list
lst1=[3.14, 66, "Teddy Bear", True, [], {}]
lst2=[]

for i in lst1:
    lst2.append(type(i))



print(lst2)

#Exercise 10: Write a while loop that adds all the numbers up to 100 (inclusive)
counter=0
total=0

while counter<=100:
    total = total+counter
    counter+= 1





print(total)

# Exercise 11: Using while loop, if statement and str() function; iterate through the list and if there is a 100, print it with its index numbe

lst=[10, 99, 98, 85, 45, 59, 65, 66, 76, 12, 35, 13, 100, 80, 95]

i = 0
while i < len(lst):
    if lst[i] == 100:
        print("There is a 100 at index no: " + str(i))
    i = i+1


# Exercise 12: Using while loop and an if statement write a function named name_adder which appends all the elements in a list to a new list unless the element is an empty string: ""

lst1=["Joe", "Sarah", "Mike", "Jess", "", "Matt", "", "Greg"]

def name_adder(list):
    i = 0
    new_list = []
    while i < len(list):
        if list[i] != "":
            new_list.append(list[i])
        i = i+1
    return new_list

print(name_adder(lst1))


# Exercise 13: This time inside a function named name_adder, write a while loop that stops appending items to the new list as soon as it encounters an empty string: "". And prints "There is an empty string and returns the new list.

lst1=["Sam", "", "Ben", "Olivia", "Alicia"]
i=0

def name_adder(list):
    i = 0
    new_list = []
    while i < len(list):
        if list[i] != "":
            new_list.append(list[i])
        else:
            break
        i = i+1
    return new_list

print(name_adder(lst1))

# Exercise 14: Write an if statement that asks for the user's name via input() function. If the name is "Bond" make it print "Welcome on board 007." Otherwise make it print "Good morning NAME"

name = input("Enter your name here: ")

if name == "Bond":
    print("Welcome on board 007")
else:
    print("Good morning "+ name)
    

# Exercise 15: Do the same thing as exercise 7-a this time making sure if the name is bond with lower case b it still prints "Welcome on board 007."

name = input("Please enter your name.")
if name.lower() == "bond":
    print("Welcome on board 007")
else:
    print("Good morning " + name)
    
    
# Exercise 16: Write a function named "evens" which returns True if a number is even and otherwise returns False

def evens(i):
    if i % 2 == 0:
        return True
    else:
        return False
    
print(evens(99))
print(evens(98))


# Exercise 17: Write a function named "thedecimal" which returns the decimal part of a number. If decimal part is zero function should return this string: "INTEGER"

def thedecimal(i):
    if i - int(i) != 0:
        return i-int(i)
    else:
        return "INTEGER"
    
print(thedecimal(99.09))
print(thedecimal(99.00))


# Exercise 18: treepersqkm is a dictionary showing the tree number of countries per square kilometer for random countries with sizeable population numbers. Write a function named "moretrees" that returns a list of country names with more than 20.000 trees per square kilometer

treepersqkm = {"Finland": 90652, "Taiwan": 69593, "Japan": 49894, "Russia": 41396, "Brazil": 39542, "Canada": 36388, "Bulgaria": 24987, "France": 24436, "Greece": 24323, "United States": 23513, "Turkey": 11126, "India": 11109, "Denmark": 6129, "Syria": 534, "Saudi Arabia": 1}

def moretrees(dict):
    lst = []
    for i in dict:
        if dict[i]>20000:
            lst.append(i)
        else:
            pass
    return lst


print(moretrees(treepersqkm))

# Exercise 19: Write a function named "count_l" that counts the number of words that contain the letter: "l" in a given string.

def count_l(a):
    c = 0
    for i in a.split():
        if "l" in i:
            c = c+1
        else:
            pass

    return c

print(count_l(str))

#Exercise 20: Write a similar function to 7-e which returns the number of words that start with letter "A" in a string. (Make sure it counts lower case a's as well.)

def count_l(a):
    c = 0
    for i in a.split():
        if i[0].lower() == a:
            c = c+1
        else:
            pass

    return c

print(count_l(str))