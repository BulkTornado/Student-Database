import json

try:
    with open(r"StudentDetails_v1_0.json") as Stud_Details_Json:
        Stud_Details_Dict = json.load(Stud_Details_Json)
        #print(json.dumps(Stud_Details_Dict,indent=4))
        print(f"{ "=" * 84}\n")
        for roll, Info in Stud_Details_Dict.items():
            totalMarks = sum( list( Info["Marks"].values() ) )
            print(f"{f"> Roll Number {roll:>02} | {Info["Name"]:^19}: { totalMarks / 2 :.2f} % <":-^84}\n")
            for sub, mark in Info["Marks"].items():
                print(f"{sub:^10}: {mark:>02}", end = " | ")
            print("\n")
            print(f"{ "=" * 84}\n")
            
except FileNotFoundError:
    print(f"File not found!!!")
    print(f"Create one using StudentDetails.py first, then run this program!!!")
