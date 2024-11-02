import time

def find_coins_greedy(amount):
    coins = [50, 25, 10, 5, 2, 1]
    change = {}
    start_time = time.time()
    for coin in coins:
        if amount >= coin:
            num_coins = amount // coin
            change[coin] = num_coins
            amount -= num_coins * coin
    end_time = time.time()
    print("Час виконання жадібного алгоритму:", end_time - start_time)
    return change

def find_min_coins(amount):
    coins = [50, 25, 10, 5, 2, 1]
    dp = [float('inf')] * (amount + 1)
    dp[0] = 0
    start_time = time.time()
    for coin in coins:
        for i in range(coin, amount + 1):
            dp[i] = min(dp[i], dp[i - coin] + 1)
    change = {}
    for coin in coins:
        while amount >= coin and dp[amount] == dp[amount - coin] + 1:
            amount -= coin
            change[coin] = change.get(coin, 0) + 1
    end_time = time.time()
    print("Час виконання алгоритму динамічного програмування:", end_time - start_time)
    return change

# Приклад використання:
amount = 113
print("Жадібний алгоритм:", find_coins_greedy(amount))
print("Алгоритм динамічного програмування:", find_min_coins(amount))