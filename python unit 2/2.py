def fibonacci_string(n):
    "Generate Fibonacci string sequence up to n terms"
    if n <= 0:
        return []
    elif n == 1:
        return ["A"]
    elif n == 2:
        return ["A", "B"]

    seq = ["A", "B"]
    for i in range(2, n):
        seq.append(seq[i-1] + seq[i-2])   
    return seq


n = int(input("Enter number of terms: "))
result = fibonacci_string(n)

print("Fibonacci String Sequence:")
for s in result:
    print(s)
