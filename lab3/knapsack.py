def knapsack_bottom_up(weights, profits, capacity):
    # initialize a dp table with size capacity + 1, all set to 0
    dp = [0] * (capacity + 1)

    # iterate through each capacity from 1 to the given capacity
    for c in range(1, capacity + 1):
        current_best_profit = 0  # initialize the best profit for this capacity
        # check each item to see if it can fit into the current capacity
        for i in range(len(weights)):
            item_weight = weights[i]
            item_profit = profits[i]
            if item_weight <= c:
                remaining_capacity = c - item_weight
                # update the best profit for this capacity
                current_best_profit = max(current_best_profit, item_profit + dp[remaining_capacity])
        dp[c] = current_best_profit  # store the best profit for this capacity

    # return the maximum profit for the given knapsack capacity
    return dp[capacity]



#testing inputs for part a

weights=[4,6,8] #weight of each item
profits=[7,6,9] #profit of each item
capacity=14 #capacity of the knapsack

max_profit = knapsack_bottom_up(weights, profits, capacity)

# print output in table format
print("\n" + "="*50)
print("KNAPSACK PROBLEM - BOTTOM-UP APPROACH")
print("="*50)
print("\nITEMS:")
print("-"*50)
print(f"{'Item':<10} {'Weight':<15} {'Profit':<15}")
print("-"*50)
for i in range(len(weights)):
    print(f"{'Item ' + str(i+1):<10} {weights[i]:<15} {profits[i]:<15}")
print("-"*50)
print(f"\n{'Knapsack Capacity:':<30} {capacity}")
print(f"{'Maximum Profit:':<30} {max_profit}")
print("="*50 + "\n")


#testing inputs for part b

weights=[5,6,8] #weight of each item
profits=[7,6,9] #profit of each item
capacity=14 #capacity of the knapsack

max_profit = knapsack_bottom_up(weights, profits, capacity)

# print output in table format
print("\n" + "="*50)
print("KNAPSACK PROBLEM - BOTTOM-UP APPROACH")
print("="*50)
print("\nITEMS:")
print("-"*50)
print(f"{'Item':<10} {'Weight':<15} {'Profit':<15}")
print("-"*50)
for i in range(len(weights)):
    print(f"{'Item ' + str(i+1):<10} {weights[i]:<15} {profits[i]:<15}")
print("-"*50)
print(f"\n{'Knapsack Capacity:':<30} {capacity}")
print(f"{'Maximum Profit:':<30} {max_profit}")
print("="*50 + "\n")