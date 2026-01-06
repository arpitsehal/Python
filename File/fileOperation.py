# f = open("File/sample.txt", "r") # Open a file in read mode
# content = f.read()          # Read the content of the file
# print(content)              # Print the content to the console
# f.close()                  # Close the file


f = open("File/sample.txt", "w") # Open a file in write mode
f.write("Hello, World!")         # Write data to the file
print("Data written to file.")
f.close()                  # Close the file 