# Dictionaries

fruits = {
    1: "pomogranate",
    2: "apple",
    3: "guava",
    4: "banana"

}
print(fruits)

print(fruits[4])

fruits[5] = "lichi"
print(fruits)

empty = {}

fruits[2] = "watermelon"
print(fruits)


for key in fruits:
    print(key)


# grading system

students = {
    "kajal": 89,
    "mahesh": 76,
    "suresh": 23,
    "rahul": 99,
    "akash": 45,
    "vishal": 90
}

marks = {}

for key in students:
    score = students[key]
    if score > 90:
        marks[key] = "outstanding"
    elif score > 80:
        marks[key] = "average"
    elif score > 45:
        marks[key] = "fine"
    else:
        marks[key] = "poor"


print(marks)
