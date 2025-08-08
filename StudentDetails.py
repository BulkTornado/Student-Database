import json

def EnterDetails():
    try:
        with open(r"StudentDatabase_v1_0.json", "r") as Stud_Details_Json:
            Stud_Details_Dict = json.load(Stud_Details_Json)
        num = int(input("How many students: "))
        if num <= 0:
            print("Next time, enter a value more than 0")
        else:
            with open(r"StudentDatabase_v1_0.json", "w") as Stud_Details_Json:
                for i in range(num):
                    try:
                        print(f"-------------------------------\nIteration {i+1}")
                        Stud_Details_Dict.update({int(input("Roll: ")): {"Name": input("Name: "), "Class": input("Class: "), "Section":input("Section: "),
                                                                         
                                                                         "Marks": { "Physics": int(input("Phy: ")),
                                                                                   "Chemistry": int(input("Chem: ")),
                                                                                   "Maths": int(input("Maths: ")),
                                                                                   "Comp Sci": int(input("CS: ")),
                                                                                   "English": int(input("Eng: "))
                                                                        } } } )
                    except ValueError:
                        print("OOPS!!! Invalid input, try again")
                json.dump(Stud_Details_Dict, Stud_Details_Json, indent = 4)
    except FileNotFoundError:
        print(f"File not found! Creating new one!!!")
        with open(r"StudentDetails_v1_0.json", "w") as Stud_Details_Json:
            json.dump({}, Stud_Details_Json, indent = 4)
        print(f"File successfully created and closed")
        print(f"Run program again")
    except ValueError:
        print("Enter a number!!!")
    # No need for the following except clause if the data is in .json file. 
    # Used this one when the details was in a text file. 
    # First, I was reading the whole file, then using eval() function to convert it into a dictionary, 
    # so this was important here.
    except SyntaxError: 
        print(f"File found to be empty or in wrong syntax!")
        print(f"Fixing the syntax now!")
        with open(r"StudentDetails_v1_0.json", "w") as Stud_Details_Json:
            json.dump({}, Stud_Details_Json, indent = 4)
        print(f"Syntax fixed successfully!")
        print(f"Run program again")

def SeeDetails():
    try:
        with open(r"StudentDatabase_v1_0.json", "r") as Stud_Details_Json:
            Stud_Details_Dict = json.load(Stud_Details_Json)
        # Quickly checking if data is empty
        if len(Stud_Details_Dict) == 0:
            raise
        print("Enter 0 to view all the details, else enter a valid roll number...")
        roll = int(input("Roll number: "))
    except FileNotFoundError:
        print(f"Database doesn't exist!!!")
        print(f"Enter choice as 1 and create a database first...")
    except ValueError:
        print(f"Enter a number!!!")
    # No need for the following except clause if the data is in .json file. 
    # Used this one when the details was in a text file. 
    # First, I was reading the whole file, then using eval() function to convert it into a dictionary, 
    # so this was important here.
    except SyntaxError:
        print(f"File found to be empty or in wrong syntax!")
        print(f"Fixing the syntax now!")
        with open(r"StudentDetails_v1_0.json", "w") as Stud_Details_Json:
            json.dump({}, Stud_Details_Json, indent = 4)
        print(f"Syntax fixed successfulyly!")
        print(f"Run program again")
    # When error raised forcefully using 'raise' statement
    except:
        print(f"Database found to be empty!!!")
        print(f"Enter choice as 1 and and create a database first...")
    
    else:
        roll = str(roll)
        if roll == "0":
            print(json.dumps(Stud_Details_Dict, indent=4))
        else:
            try:
                print(f"Roll {roll:>02}:\n", json.dumps(Stud_Details_Dict[roll], indent=4))
            except KeyError:
                print(f"Roll {roll:>02} doesn't exist in database! Enter the student's details first!")
                
def ClearDetails():
    try:
        with open(r"StudentDatabase_v1_0.json", "w") as Stud_Details_Json:
            json.dump({}, Stud_Details_Json, indent = 4)
        print(f"Data cleared")
    except FileNotFoundError:
        print("File does not exist!!!")
        print(f"Enter choice as 1 and create a database first...")

def menu():
    ListChoices = ["Exit","Enter Details", "See Details", "Clear all details"]
    for index, val in enumerate(ListChoices, 0):
        print(f"{index}. {val}")
    try:
        choice = int(input("Choice? "))
    except ValueError:
        print("Enter a number!!!")
    else:
        if choice == 1:
            EnterDetails()
        elif choice == 2:
            SeeDetails()
        elif choice == 3:
            ClearDetails()
        elif choice == 0:
            print(f"{" Leaving ":=^150}")
        else:
            print(f"{" Enter valid choice!!! ":=^150}")

# To view the entire file content quickly
def ShowEntireQuick(): 
    with open(r"StudentDetails_v1_0.json", "r") as Stud_Details_Json:
        print(json.dumps(json.load(Stud_Details_Json), indent = 4))

menu()
#ShowEntireQuick()
