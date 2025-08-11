from json import load, dump, JSONDecodeError
from time import sleep

def Subjects():
    return ["Physics", "Chemistry", "Maths", "Comp Sci", "English"]

def Exams():
    return ["Periodic Test 01", "Periodic Test 02", "Periodic Test 03", "Periodic Test 04"]

def menu():
    return ["Exit","Update Database", "Update a Student's record", "Look-up a Student's Record", "Delete a Student's Record", "Delete the entire database"]

def InputExamMarks():
    Marks = {}
    for exam in Exams():
        print("=" * 42)
        Temp_Sub_Marks = {}
        for sub in Subjects():
            Temp_Sub_Marks.update({sub: int(input(f"{f"{exam:^18} | {sub:^10}: ":^40}"))})
        Marks.update({exam: Temp_Sub_Marks})
    else:
        print("=" * 42)
    return Marks

def UpdateDatabase(Dict):
    try:
        Stud_Details_Dict = Dict
        Stud_Count = int(input("Student Count: "))
        if Stud_Count <= 0:
            raise ValueError
        for i in range(1, Stud_Count + 1):
            print(f"{"   Student: " + f"{ i :>02}   ":*^100}")
            Roll = int(input("Enter roll: "))
            if str(Roll) in Stud_Details_Dict:
                raise KeyError
            if Roll <= 0:
                raise ValueError
            Name = input("Name: ")
            Marks = InputExamMarks()
            Stud_Details_Dict.update( {Roll: {"Name": Name, "Marks": Marks}} )
            sleep(1)
    except ValueError:
        print("Enter an integer value greater than 0!!!")
    except KeyError:
        print(f"Student with roll number {Roll:02} already exists in database, use option 2 to update the student's data instead...")
    else:
        with open(r"StudentDatabase_v2_0.json", "w") as Stud_Details_File:
            dump(Stud_Details_Dict, Stud_Details_File, indent = 4)
        print("Database updated")
    return

def UpdateStudent(Dict):
    try:
        Stud_Details_Dict = Dict
        Roll = int(input("Enter roll: "))
        if Roll <= 0:
            raise ValueError
        if str(Roll) not in Stud_Details_Dict:
            raise KeyError
        Stud_Details_Dict_Copy = {}
        Roll = str(Roll)
        Name = input("Name: ")
        Marks = InputExamMarks()
        for rolls in Stud_Details_Dict:
            if rolls != Roll: Stud_Details_Dict_Copy.update({rolls: Stud_Details_Dict[rolls] })
            else: Stud_Details_Dict_Copy.update({Roll: {"Name": Name, "Marks": Marks}})
    except ValueError:
        print("Enter an integer value greater than 0!!!")
    except KeyError:
        print(f"Student with roll number {Roll:02} doesn't exist in database, use option 1 to add the student first...")
    else:
        with open(r"StudentDatabase_v2_0.json", "w") as Stud_Details_File:
            dump(Stud_Details_Dict_Copy, Stud_Details_File, indent = 4)
    return

def SearchStudent(Dict):
    try:
        import StudentMarks_v2_0
        print("Enter 0 to view all details, else enter a valid roll number...")
        Roll = int(input("Enter roll number: "))
    except ModuleNotFoundError:
        print("Module not found, can't print the data with formatting...")
    except ValueError:
        print("Enter a valid number")
    else:
        StudentMarks_v2_0.main(Dict, RollNo = Roll) #Roll number not existing in database is handled by the module itself
    return

def DeleteStudent(Dict):
    try:
        import StudentMarks_v2_0
        Stud_Details_Dict = Dict
        Roll = int(input("Enter roll number: "))
        if Roll <= 0:
            raise ValueError
        if str(Roll) not in Stud_Details_Dict:
            raise KeyError
        StudentMarks_v2_0.main(Roll)
        print("Do you wish to proceed with deleting this student's records (y/n)?")
        choice = input().strip().lower()[0]
        match choice:
            case "y":
                del Stud_Details_Dict[str(Roll)]
                print("Student's record deleted from database!")
            case "n":
                print("Aborting program...")
    except ValueError:
        print("Enter an integer value greater than 0!!!")
    except KeyError:
        print(f"{Roll:>02} not found in database!!!")
    else:
        with open(r"StudentDatabase_v2_0.json", "w") as Stud_Details_File:
            dump(Stud_Details_Dict, Stud_Details_File, indent = 4)

def DeleteDatabse():
    try:
        with open(r"StudentDatabase_v2_0.json", "w") as Stud_Details_File:
            print("Database located, deleting it now...")
            Stud_Details_File.close()
        sleep(2); print("Database deleted!")
    except FileNotFoundError:
        print("Database not found!!!")
    return

def main(ListChoice, Dict):
    try:
        for index, val in enumerate(ListChoice, 0):
            print(f"{index}. {val}")
        choice = int(input("\nEnter choice: "))
    except ValueError:
        print("Enter valid number for choice")
    else:
        match choice:
            case 0:
                print("Exiting program...")
            case 1:
                UpdateDatabase(Dict)
            case 2:
                UpdateStudent(Dict)
            case 3:
                SearchStudent(Dict)
            case 4:
                DeleteStudent(Dict)
            case 5:
                DeleteDatabse()
            case _:
                print("Enter valid choice")
    return

if __name__ == "__main__":
    print(f"\n{"   Database manager ONLY for a specific class and section   ":*^100}\n")
    sleep(3)
    try:
        print("Looking for database...")
        sleep(1)
        with open(r"StudentDatabase_v2_0.json", "r") as File:
            Database = load(File)
        print("Database located...\n")
    except JSONDecodeError:
        print("\nDatabase is empty, or has been tampered with, in that case manually fix it...")
        print("Stopping all operations...")
    except FileNotFoundError:
        print("\nDatabase not found!!!")
        print("Stopping all operations...")
    else:
        main(menu(), Database)
