from json import load, JSONDecodeError
from time import sleep

def printFormat(Roll, Info):
    print(f"{" Roll: " + f"{Roll:>02}" + " | Name: " + f"{Info["Name"]:^30} ":=^100}\n")
    _Index = 0
    for exam in list(Info["Marks"].keys()):
        print(f"{exam}\n|", end="")
        for sub, mark in list(Info["Marks"].values())[_Index].items():
            print(
                f"{sub:^10}: {mark:>02}/{40 if exam.split()[-1] in ("01", "03") else 80 if sub in ("Maths", "English") else 70}",
                end=" | ")
        _Index += 1
        print("\n")
    print(f"{"=" * 100}\n")
    print(f"{"*" * 100}\n")
    return

def main(Dict, RollNo = 0):
    try:
        Stud_Details_Dict = Dict
        RollNo = str(RollNo)
        if RollNo != "0" and RollNo not in Stud_Details_Dict:
            raise KeyError
    except ValueError: #This is here in case someone passes a 'str' value directly in this module itself
        print("Enter a valid roll number!!!")
    except KeyError:
        print(f"No student with roll number {RollNo:>02} exists in database")

    else:
        if RollNo == "0":
            print("Loading database..."); sleep(1.5)
            print("Database loaded, printing...\n"); sleep(1.5)
            print(f"{ "*" * 100}\n")
            for roll, Info in Stud_Details_Dict.items():
                printFormat(roll, Info); sleep(0.5)
        else:
            print("Searching for student, please wait..."); sleep(1.5)
            print("Student's data found, printing...\n"); sleep(1.5)
            print(f"{ "*" * 100}\n")
            Info = Stud_Details_Dict[RollNo]
            printFormat(RollNo, Info)
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
        main(Database)
