word = "artificial intelligence"

count = 0
for char in word:
    if(char == 'i'):
        count += 1

print(f"The letter 'i' appears {count} times in the word '{word}'.")