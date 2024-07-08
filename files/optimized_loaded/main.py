from data_loader import load_actions
from knapsack import knapsack
from display import display_results


def main():
    actions = load_actions("data/dataset2_Python+P7.csv")
    max_profit, selected_items, total_budget_used, elapsed_time = knapsack(actions, 500)
    display_results(selected_items, max_profit, total_budget_used, elapsed_time)


if __name__ == "__main__":
    main()
