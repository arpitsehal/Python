# try is a code block that lets you test a block of code for errors.
#except lets you handle the error.
#else lets you execute code when there is no error.
#finally lets you execute code, regardless of the result of the try- and except blocks.

try: 
    x = int(input("Enter x: "))
    ans = 10 / x
except ZeroDivisionError:
    print("Error: Division by zero is not allowed.")
except ValueError:
    print("Error: Invalid input. Please enter a numeric value.")
else:
    print("The answer is:", ans)
finally:
    print("Execution completed.")
    