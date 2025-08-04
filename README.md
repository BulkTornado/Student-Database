# Student Database

A simple Python program(or maybe not so simple) that reads the data from a json file, and presents it to the user in a readable format.

Currently, two version have been built, with more versions to come.


## Instructions

- To view all of the versions, head to the release page(on this right side of the screen) or click the following link: [**Release Page**](https://github.com/BulkTornado/Student-Database/releases)
- Fundamentally, each version is completely different(I hope so). As such, with each release, there **WILL** be a note detailing the changes made.
- **REMEMBER**, each version [might] have different dependencies. This means that for each version, the data structure and functionality is different(more on it in the upcoming section). As such, read the note and see what are the **_required_** dependencies that you **NEED** to download and **_optional_** dependencies which you can skip if you want, however it is highly recommended that you download everything for optimal experience(I guess :>).
- Once you have understood everything, you can download any version of the program which is suitable for your use.

## Data structure

- Depending on the version you are using, the data structure is completely different.
- As such, every version of the program requires it's unique file.
- No version's database is compatible with any other version's Python program(at least till version 2.0, when I am currently writing this).
Here's a example:
#### Version 1.0 data structure
```json
{
    "1": {
        "Name": "XYZ",
        "Class": "12",
        "Section": "A",
        "Marks": {
            "Physics": 37,
            "Chemistry": 38,
            "Maths": 31,
            "Comp Sci": 28,
            "English": 29
        }
    }
}
```
#### Version 2.0 data structure
```json
{
    "1": {
        "Name": "XYZ",
        "Class": "12",
        "Section": "A",
        "Marks": {
            "Periodic Test 01": {
                "Physics": 37,
                "Chemistry": 38,
                "Maths": 31,
                "Comp Sci": 28,
                "English": 29
            },
            "Periodic Test 02": {
                "Physics": 72,
                "Chemistry": 75,
                "Maths": 79,
                "Comp Sci": 70,
                "English": 73
            },
            "Periodic Test 03": {
                "Physics": 35,
                "Chemistry": 36,
                "Maths": 29,
                "Comp Sci": 26,
                "English": 27
            },
            "Periodic Test 04": {
                "Physics": 73,
                "Chemistry": 72,
                "Maths": 77,
                "Comp Sci": 72,
                "English": 76
            }
        }
    }
}
```

## Future Ideas

- I would like to change the database yet again in version 3.0, to support class wise segregation.
- This is a major hiccup right now cuz only roll numbers are used to search for a student, and the class and section in the database is used only to make the output nicer :)
- In version 4.0, I would like to introduce the key as a tuple containing the Board(CBSE/ICSE/any other), School Code(CBSE/ICSE/any other), and School Name, and work from there. Let's see how I will be able to implement that :)
