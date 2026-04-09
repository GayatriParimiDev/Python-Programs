# This is a Python program to count the number of ways to make exact change for a given price using specified coin denominations.

def count_change_combinations(coins, price):
    dp = [0] * (price + 1)
    dp[0] = 1  
    for coin in coins:
        for amount in range(coin, price + 1):
            dp[amount] += dp[amount - coin]
    return dp[price]

if __name__ == "__main__":
    
    try:
        price = int(input("Enter the target value: "))
    except ValueError:
        print("Please enter a valid integer value.")
        exit(1)

    coins = [1, 2, 5]  

    combinations = count_change_combinations(coins, price)
    print(f"Number of ways to make exact change for {price} : " , combinations)