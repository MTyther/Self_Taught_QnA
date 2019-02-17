print("Question 1:")
bookQuote = """
\"There is no greater agony than bearing an untold story inside you.\"
by
Maya Angelou: \"I Know Why the Caged Bird Sings\""""

print(bookQuote)

print("\n")
print("Question 2:")
before_slice = """It was a bright cold day in April, and the clocks were striking thirteen."""
print("Before slice: " + before_slice)
after_slice = before_slice[0:before_slice.index(",")]
print("After slice: " + after_slice + ".")

print("\n")
print("Question 3:")
word_list = ["The", "fox", "jumped", "over", "the", "fence", "."]
sentence = " ".join(word_list)
new_sentence = sentence.replace(" .", ".")
print("Word List: " + str(word_list))
print("Sentence: " + sentence)
print("New sentence: " + new_sentence)