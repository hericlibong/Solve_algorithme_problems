import pandas as pd


def load_actions(filename):
    data = pd.read_csv(filename)
    data.columns = ['Actions', 'Cost', 'Profit']
    data['Cost'] = pd.to_numeric(data['Cost'], errors='coerce').abs()
    data['Profit'] = pd.to_numeric(data['Profit'], errors='coerce')
    data.dropna(inplace=True)
    # Filtrer les actions avec un coût strictement positif
    data = data[data['Cost'] > 0.001]  # Augmenter légèrement le seuil pour exclure les coûts extrêmement bas
    return data
