# Exercise 1: Print first 10 natural numbers
i = 1
while i <= 10:
    print(i)
    i += 1
    
 
# Exercise 2:    
row = 5
for i in range(1, row + 1, 1):
    for j in range(1, i + 1):
        print(j, end=' ')
    print("")
    
    
# Exercise 3: Write a program to print multiplication table of a given number
n = 2
for i in range(1, 11, 1):
    product = n * i
    print(product)
    
    
# Exercise 4: Display numbers from a list using loop
numbers = [12, 75, 150, 180, 145, 525, 50]

for num in numbers:
    if num > 500:
        break
    elif num > 150:
        continue
    # check if number is divisible by 5
    elif num % 5 == 0:
        print(num)
        
        
# Exercise 5: Count the total number of digits in a number
num = 75869
counter = 0

while num != 0:
    num = num//10
    counter += 1
print(counter)


# Exercise 6: Print list in reverse order using a loop 
mylist = [10, 20, 30, 40, 50]
new_list = reversed(mylist)
for num in new_list:
    print(num)
    
    
# Exercise 7: Display numbers from -10 to -1 using for loop
for num in range(-10, 0, 1):
    print(num)
    
    
# Exercise 8: Use else block to display a message “Done” after successful execution of for loop
for i in range(5):
    print(i)
else:
    print("Done!")
    
    
# Exercise 9: Fibonacci sequence
def fib(n):
    a = 0
    b = 1
    if n == 1:
        print(a)
    else:
        print(a)
        print(b)
        
        for i in range(2, n):
            c = a+b
            a = b
            b = c
            print(c)
fib(10)


# Exercise 10: Find the factorial of a given number
def fact(n):
    f = 1
    for i in range(1, n+1):
        f = f*i
    return f
result = fact(5)
print(result)
