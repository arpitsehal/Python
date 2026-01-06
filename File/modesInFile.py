#read mode
# f = open("File/sample.txt", "r") # Open a file in read mode
# content = f.read()          # Read the content of the file
# print(content)              # Print the content to the console
# f.close()                  # Close the file

#write mode
# f = open("File/sample.txt", "w") # Open a file in write mode
# f.write("Hello, World!")         # Write data to the file
# print("Data written to file.")
# f.close()                  # Close the file

#append mode
# f = open("File/sample.txt", "a") # Open a file in append mode
# f.write("\nAppended line.")       # Append data to the file 
# print("Data appended to file.")
# f.close()                  # Close the file

# #xclusive creation mode
# f = open("File/newfile.txt", "x") # Create a new file in
# f.write("This file is created in exclusive creation mode.") # Write data to the new file
# print("New file created and data written.")
# f.close()                  # Close the file

# # #binary mode
# f = open("File/sample.bin", "wb") # Open a binary file in write mode
# f.write(b'\x00\xFF\x00\xFF')      # Write binary data
# print("Binary data written to file.")
# f.close()                  # Close the file

# read and write mode
f = open("File/sample.txt", "r+") # Open a file in read and write mode
content = f.read()                # Read the content of the file
print("Before writing:", content) # Print the content to the console
f.write("\nAdding a new line.")   # Write data to the file
f.seek(0)                        # Move the cursor to the beginning of the file
content = f.read()                # Read the updated content of the file
print("After writing:", content)  # Print the updated content to the console
f.close()                        # Close the file
