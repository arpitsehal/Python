color = input("Enter a color: ")

match color:
    case "red":
        print("Stop.")
    case "yellow":
        print("Look.")
    case "green":
        print("Go.")
    case _:                     #default case
        print("Invalid color.")
         