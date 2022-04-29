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