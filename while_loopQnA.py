# Question 1
print("Question 1")
numbers = ["25", "5", "9", "18", "2"]
while True:
    guess = input("Guess a number or q to quit! ")
    if guess == "q":
        print("Ok, you ended the game, goodbye!")
        break
    if guess in numbers:
        print("Great, you guessed '{}' corrrectly".format(guess))
        continue
    if guess not in numbers:
        print("Sorry, you guessed wrong!")
        continue

# Question 2
print("\nQuestion 2")
list1 = [8, 19, 148, 4]
list2 = [9, 1, 33, 83]
sumlist = []
for i in list1:
    for j in list2:
        sumlist.append(i * j)

print("List1 * List2 = '{}'".format(sumlist))

