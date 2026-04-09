academic_record = {}

def add_course(course, credits, points):
    "Add a new course with total credits and earned points"
    academic_record[course] = {"credits": credits, "points": points}

def drop_course(course):
    "Remove a course from the record"
    if course in academic_record:
        del academic_record[course]

def print_record():
    "Print all academic records"
    if not academic_record:
        print("No courses available.")
    else:
        print("Course\tCredits\tPoints")
        for course, data in academic_record.items():
            print(f"{course}\t{data['credits']}\t{data['points']}")

def calculate_cgpa():
    "Calculate CGPA = sum(credits * points) / sum(credits)"
    if not academic_record:
        return 0.0
    total_credits = sum(data["credits"] for data in academic_record.values())
    weighted_sum = sum(data["credits"] * data["points"] for data in academic_record.values())
    return weighted_sum / total_credits if total_credits > 0 else 0.0
