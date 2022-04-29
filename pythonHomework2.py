
# Exercise 1: Write a Python program to find those numbers which are divisible by 7 and multiple of 5, between 1500 and 2700 (both included)
for i in range(1500, 2701):
    if i % 7 == 0 and i % 5 == 0:
        print(i)
        
        
# Exercise 2: Guess the correct number
import random

target_num = random.randint(1, 10)
guess_num = 0
while target_num != guess_num:
    guess_num = int(input('Guess a number between 1 and 10 until you get it right : '))
print('Well guessed!')


# Exercise 3: fizzbuzz

for i in range(51):
    if i % 3 == 0 and i % 5 == 0:
        print("Fizzbuzz")
    elif i % 5 == 0:
        print("buzz")
    elif i % 3 == 0:
        print("fizz")
    else:
        print(i)
        
# Exercise 4: Write a Python program to calculate a dog's age in dog's years
human_age = int(input("Input a dog's age in human years: "))

if human_age <= 2:
    dog_age = human_age * 10.5
else:
    dog_age = 21 + (human_age - 2)*4

print("The dog's age in dog's years is", dog_age)


# Exercise 5: Write a Python program to check whether an alphabet is a vowel or consonant
letter = input("please enter a letter: ")
if letter != 'a' and letter!= 'e' and letter!= 'i' and letter!= '0' and letter!= 'u':
    print(letter + " is a consonant")
else:
    print(letter + " is a vowel")