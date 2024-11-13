# GitLA13 Project

print("A - Add Record")
print("B - View Records")
print("C - Clear All Records")
print("D - Exit")
choice = ""
while choice.upper() != 'D':
    choice = input("ENTER SELECTION [A, B, C, or D]: ")
    if choice.upper() == 'A':
        print("Add Record")
        addRec()
    elif choice.upper() == 'B':
        print("View Records")
        viewRec()
    elif choice.upper() == 'C':
        print("Clear All Records")
        clearRec()
    elif choice.upper() == 'D':
        print("Thank you!")

    def addRec():
        filename = "records.txt"  
        name = input("Enter Name: ")
        email = input("Enter Email: ")
        addr = input("Enter Address: ")
        
        with open(filename, 'a') as file:
            file.write(name + ", " + email + ", " + addr + "\n")
            print("Record added successfully!")

    def viewRec():
         filename = "records.txt"  
    
    try:
        with open(filename, 'r') as read_file:
            print(read_file.read())
    except FileNotFoundError:
        print("The file does not exist. Please make sure the file is available.")

    def clearRec():
        filename = "records.txt"  
        with open(filename, 'w') as file:
             pass
        print("All records have been cleared.")

    def viewRec():
        filename = "records.txt"  
    
    try:
       
        with open(filename, 'r') as read_file:
            print(read_file.read())
    except FileNotFoundError:
        print("The file does not exist. Please make sure the file is available.")
