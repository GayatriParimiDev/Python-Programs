def compute_cgpa(filename):
    try:
        total_points_sum = 0
        total_credits_sum = 0

        with open(filename, 'r') as file:
            for line in file:
                parts = line.strip().split()
                if len(parts) != 3:
                    continue  # skip lines not matching format
                
                course, points_str, credits_str = parts
                points = float(points_str)
                credits = float(credits_str)

                total_points_sum += points
                total_credits_sum += credits

        if total_credits_sum == 0:
            print("No credits found, cannot compute CGPA.")
            return

        cgpa = total_points_sum / total_credits_sum
        print(f"Computed CGPA: {cgpa:.2f}")

    except FileNotFoundError:
        print(f"File '{filename}' not found.")
    except ValueError:
        print("Error in file format: ensure points and credits are numbers.")

compute_cgpa('records.txt')
