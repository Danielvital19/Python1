text = input("enter a text: ")
letters = []

text = text.lower()

letters.append(input("enter the first letter: ").lower())
letters.append(input("enter the second letter: ").lower())
letters.append(input("enter the third letter: ").lower())

print("\n")
print("Letters")

letters_count1 = text.count(letters[0])
letters_count2 = text.count(letters[1])
letters_count3 = text.count(letters[2])

print(f"there are {letters_count1} {letters[0]}'s")
print(f"there are {letters_count2} {letters[1]}'s")
print(f"there are {letters_count3} {letters[2]}'s")

print("\n")
print("Words")

words = text.split()
print(f"There are {len(words)} words in the text")

print("\n")
print("Initial and final letters")

first_letter = text[0]
last_letter = text[-1]

print(f"the initial letter is: {first_letter}")
print(f"the final letter is: {last_letter}")

print("\n")
print("Reverse text")
words.reverse()
reverse_text = ' '.join(words)
print(f"Reverse text: {reverse_text}")