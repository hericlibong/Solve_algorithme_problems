import time


def knapsack(actions, max_budget):
    start_time = time.perf_counter()
    dp = [0 for _ in range(max_budget + 1)]
    item_selection = [[] for _ in range(max_budget + 1)]
    budget_used = [0 for _ in range(max_budget + 1)]

    for i in range(len(actions)):
        cost = float(actions.iloc[i]['Cost'])
        if cost < 0.01:  # Exclure les coûts infimes pour des raisons pratiques
            continue
        profit = cost * (actions.iloc[i]['Profit'] / 100)
        # Parcourir de l'arrière pour éviter de revisiter la même action
        for w in range(max_budget, int(cost - 1), -1):
            new_profit = profit + dp[w - int(cost)]
            new_budget_used = budget_used[w - int(cost)] + cost
            if new_budget_used <= max_budget and new_profit > dp[w]:
                dp[w] = new_profit
                item_selection[w] = item_selection[w - int(cost)] + [(actions.iloc[i]['Actions'], cost, profit)]
                budget_used[w] = new_budget_used

    elapsed_time = time.perf_counter() - start_time
    # Trouver le meilleur budget utilisé qui reste sous le maximum
    best_budget = max((i for i in range(max_budget + 1) if budget_used[i] <= max_budget), key=lambda x: dp[x])
    return dp[best_budget], item_selection[best_budget], budget_used[best_budget], elapsed_time
