

import json

def cgpa(courses):
    total_cp = sum(c["credits"] * c["points"] for c in courses.values())
    total_c = sum(c["credits"] for c in courses.values())
    return (total_cp / total_c) if total_c else 0.0

def main():
    path = "academics.json"
    try:
        with open(path, "r", encoding="utf-8") as f:
            courses = json.load(f)
    except FileNotFoundError:
        # Seed a default record if missing so the script runs first time
        courses = {"Python": {"credits": 4, "points": 9}, "Maths": {"credits": 3, "points": 8}}
        with open(path, "w", encoding="utf-8") as f:
            json.dump(courses, f, indent=2)

    print("Loaded courses:", courses)
    print(f"Computed CGPA: {cgpa(courses):.2f}")

if __name__ == "__main__":
    main()
