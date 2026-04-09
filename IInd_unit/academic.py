
courses = []

def add_course(name, credits, points):
    courses.append((credits, points))

def calculate_cgpa():
    total_credits = sum(c[0] for c in courses)
    total_points = sum(c[0] * c[1] for c in courses)
    if total_credits == 0:
        return 0
    return total_points / total_credits