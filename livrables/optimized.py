import time

# Liste des actions
actions = [
    {"name": "Action-1", "cost": 20, "profit": 5},
    {"name": "Action-2", "cost": 30, "profit": 10},
    {"name": "Action-3", "cost": 50, "profit": 15},
    {"name": "Action-4", "cost": 70, "profit": 20},
    {"name": "Action-5", "cost": 60, "profit": 17},
    {"name": "Action-6", "cost": 80, "profit": 25},
    {"name": "Action-7", "cost": 22, "profit": 7},
    {"name": "Action-8", "cost": 26, "profit": 11},
    {"name": "Action-9", "cost": 48, "profit": 13},
    {"name": "Action-10", "cost": 34, "profit": 27},
    {"name": "Action-11", "cost": 42, "profit": 17},
    {"name": "Action-12", "cost": 110, "profit": 9},
    {"name": "Action-13", "cost": 38, "profit": 23},
    {"name": "Action-14", "cost": 14, "profit": 1},
    {"name": "Action-15", "cost": 18, "profit": 3},
    {"name": "Action-16", "cost": 8, "profit": 8},
    {"name": "Action-17", "cost": 4, "profit": 12},
    {"name": "Action-18", "cost": 10, "profit": 14},
    {"name": "Action-19", "cost": 24, "profit": 21},
    {"name": "Action-20", "cost": 114, "profit": 18},
]

def knapsack(actions, max_budget):
    start_time = time.perf_counter()
    dp = [0 for _ in range(max_budget + 1)]
    item_selection = [[] for _ in range(max_budget + 1)]
    budget_used = [0 for _ in range(max_budget + 1)]

    for i in range(len(actions)):
        cost = actions[i]['cost']
        if cost < 0.01:  # Exclure les coûts infimes pour des raisons pratiques
            continue 
        profit = cost * (actions[i]['profit'] / 100)
        # Parcourir de l'arrière pour éviter de revisiter la même action
        for w in range(max_budget, int(cost - 1), -1):
            new_profit = profit + dp[w - int(cost)]
            new_budget_used = budget_used[w - int(cost)] + cost
            if new_budget_used <= max_budget and new_profit > dp[w]:
                dp[w] = new_profit
                item_selection[w] = item_selection[w - int(cost)] + [(actions[i]['name'], cost, profit)]
                budget_used[w] = new_budget_used

    elapsed_time = time.perf_counter() - start_time
    # Trouver le meilleur budget utilisé qui reste sous le maximum
    best_budget = max((i for i in range(max_budget + 1) if budget_used[i] <= max_budget), key=lambda x: dp[x])
    return dp[best_budget], item_selection[best_budget], budget_used[best_budget], elapsed_time

def main():
    max_profit, selected_items, total_budget_used, elapsed_time = knapsack(actions, 500)
    print("Selected actions:")
    for item in selected_items:
        print(f"Action: {item[0]}, Cost: {item[1]:.3f}€, Expected Profit: {item[2]:.2f}€")
    print(f"Total Profit: {max_profit:.2f}€")
    print(f"Total Budget Used: {total_budget_used:.2f}€")
    print(f"Temps d'exécution : {elapsed_time:.4f} sec")

if __name__ == "__main__":
    main()
 