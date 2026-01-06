#with keyword
with open("File/sample.txt", "r") as f:  # Open a file in read mode
    content = f.read()          # Read the content of the file
    print(content)              # Print the content to the console

#with is used to handle file operations more efficiently.
# It automatically takes care of closing the file after the block of code is executed, even if an error occurs.