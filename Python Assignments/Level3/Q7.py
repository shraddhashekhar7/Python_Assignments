def map_course(students, courses):
    mapped = {}
    for i in range(len(students)):
        mapped[students[i]] = courses[i]

    return mapped


students = ["Sam", "Alice", "Mona"]
courses = ["Commerce", "Science", "Computer"]
print(map_course(students, courses))
