import time
from itertools import combinations

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

# Fonction pour calculer le profit
def calculate_profit(cost, percentage):
    """Calcule le profit à partir du coût et du pourcentage de profit."""
    return round(cost * (percentage / 100), 2)

# Trouver le meilleur investissement
def find_best_investment(actions):
    """Trouve la meilleure combinaison d'investissement en respectant une contrainte budgétaire, en utilisant une force brute."""
    start_time = time.time()
    best_combination = None
    max_profit = 0
    min_cost = 0

    # Itérer sur toutes les combinaisons possibles d'actions
    for i in range(1, len(actions) + 1):
        for combination in combinations(actions, i):
            total_cost = sum(action["cost"] for action in combination)
            if total_cost <= 500:
                total_profit = sum(calculate_profit(action["cost"], action["profit"]) for action in combination)
                if total_profit > max_profit:
                    max_profit = total_profit
                    best_combination = combination
                    min_cost = total_cost

    elapsed_time = time.time() - start_time
    if best_combination:
        print("Meilleure combinaison à acheter :")
        for action in best_combination:
            print(f"{action['name']} : Coût = {action['cost']}, Profit = {calculate_profit(action['cost'], action['profit'])} euros")
        print(f"Profit total : {max_profit} euros")
        print(f"Coût total : {min_cost} euros")
    else:
        print("Aucune combinaison valide trouvée dans le budget.")
    print(f"Temps d'exécution : {elapsed_time:.2f} secondes")

# Fonction principale
def main():
    find_best_investment(actions)

if __name__ == "__main__":
    main()
