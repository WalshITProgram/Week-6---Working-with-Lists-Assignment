
# Step 1: List of courses I have taken at Walsh College

courses = [
    "systems analysis and design",
    "database design and development",
    "introduction to networking",
    "introduction to security",
    "agile project management and scrum"
]


# Step 2: Sort and print courses in uppercase

courses.sort()

for course in courses:
    print("I have taken {course.upper()} at Walsh College.")


# Save my completed courses
completed = courses.copy()


# Step 3: Add new courses for next term

courses.append("cybersecurity")
courses.append("cloud computing")
courses.append("business intelligence")

courses.sort()

print("This is my course of study with upcoming courses added:")

for course in courses:
    print(course)


# Step 4: Remove courses I already took

print("I do not have to take these courses:")

for course in completed:
    courses.remove(course)
    print(course)


# Step 5: Print courses for next term

print("I plan to take the following courses next term")

for course in courses:
    print(course)


# Step 6: Make a list of numbers divisible by 6

numbers = []

for number in range(1, 1001):
    if number % 6 == 0:
        numbers.append(number)


# Step 7: Print the first 20 numbers

print("Here are twenty numbers divisible by 6.")

for number in numbers[:20]:
    print(number)


# Step 8: Find the largest number

largest = max(numbers)


# Step 9: Print the largest number

print("The maximum value in the list is:", largest)


# Step 10: Add the 10th through 50th numbers

total = sum(numbers[9:50])

print("Here is the sum of several values in the list:", total)


# Step 11: Replace courses with the numbers list

courses = numbers
