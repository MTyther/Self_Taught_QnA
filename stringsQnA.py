#Question 1

my_string = "Camus"

for letters in my_string:
    print(letters)

print("-" * 40)

#Question 2

string1 = input("You wrote a what? ")

if string1 != "":
    string2 = input("Who did you send it to? ")
    if string2 != "":
        string_cat = """Yesterday I wrote a {}. I sent it to {}.
        """.format(string1, string2)
        print(string_cat)
    else:
        print("You are not telling. I guess it's your little secret!")
else:
    print("You did not answer the question!")

print("-" * 40)

#Question 3

sentence = "aldous Huxley was born in 1894.".capitalize()
print(sentence)

print("-" * 40)

#Question 4

now_before ="Where now? Who now? When now?"
print(now_before)
now_after = now_before.split("?")
print(now_after)

print("-" *40)

#Question 5

s_total = 0
a_sentence = "A screaming comes across the sky."
print(a_sentence)
for c in a_sentence:
    if c == "s":
        s_total += 1
        a_sentence = a_sentence.replace("s", "$")
print("Total 's' in sentence = " + str(s_total))
print(a_sentence)

print("-" * 40)

#Question 6

m_index = ("Hemingway".index("m"))
print("Index of {} in {} is {}.".format("m", "Hemingway", m_index))

print("-" * 40)

threes = "three three three"
threesplusthrees = "three three three " + "three three three"
print(threesplusthrees)
threesxthrees = "three three three " * 2
print(threesxthrees)



