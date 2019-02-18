#Question 1
print("Question 1:")
movies = ["The Walking Dead", "Entourage", "The Sopranos", "The Vampire Diaries"]
print("Movies = " + '{}'.format(movies))
for movie in movies:
    print(movie)

#Question 2
print("\nQuestion 2:")
for number in range(25, 51):
    print(number)

#Question 3
print("\nQuestion 3:")
movies = ["The Walking Dead", "Entourage", "The Sopranos", "The Vampire Diaries"]
indx = 0
for movie in movies:
    print(str(indx) + ": " + movie)
    indx += 1

print("\n")
for i, movie in enumerate(movies):
    print(str(i) + ": " + movie)
