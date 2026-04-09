from itertools import combinations

def divisor_sums(n):
    divisors = [i for i in range(1, n) if n % i == 0]
    print("Divisors of", n, ":", divisors)
    
    found = False
    for r in range(1, len(divisors)+1):
        for combo in combinations(divisors, r):
            if sum(combo) == n:
                print(" + ".join(map(str, combo)), "=", n)
                found = True
    
    if found:
        print(f"\n {n} is a Perfect Number")
    else:
        print(f"\n {n} is NOT a Perfect Number")

n = int(input("Enter a number: "))
divisor_sums(n)

