# Challenge 1

try:
    number = int(input("Enter a number: "))
    length = int(input("Enter a length: "))

  
    multiples = [number * i for i in range(1, length + 1)]

    print(multiples)
except ValueError:
    
    print("Input error: Please enter valid integers for the number and length.")

# Challenge 2
user_word = input("\nEnter a word: ")


unique_chars = []

for char in user_word:
    if not unique_chars or char != unique_chars[-1]:
        unique_chars.append(char)

result_word = "".join(unique_chars)
print(result_word)
