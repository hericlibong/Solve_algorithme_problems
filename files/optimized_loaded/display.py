from prettytable import PrettyTable


def display_results(selected_items, total_profit, total_budget_used, elapsed_time):
    table = PrettyTable()
    table.field_names = ["Action", "Cost (€)", "Expected Profit (€)"]
    for item in selected_items:
        table.add_row([item[0], f"{item[1]:.3f}", f"{item[2]:.2f}"])
    print(table)
    print(f"Total Profit: {total_profit:.2f}€")
    print(f"Total Budget Used: {total_budget_used:.2f}€")
    print(f"Elapsed Time: {elapsed_time:.2f} sec")
