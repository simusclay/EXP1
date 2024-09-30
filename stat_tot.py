import pandas as pd
from scipy.stats import mannwhitneyu

# Crea il DataFrame con i tuoi dati
# data = {
#     'Group': ['A', 'A', 'A', 'B', 'B', 'B', 'B', 'B', 'B', 'C', 'C', 'C', 'C', 'C', 'D', 'D', 'D', 'D', 'E', 'E', 'E', 'F', 'F', 'F', 'F', 'G', 'G', 'G', 'G', 'G', 'H', 'H', 'H', 'I', 'I', 'I', 'J', 'J', 'J', 'K', 'K', 'K', 'K', 'L', 'L', 'L', 'L'],
#     'Rate': [0.666666667, 1, 1, 0, 0.5, 0.666666667, 0.5, 0.666666667, 0.5, 0.666666667, 1, 0.333333333, 0.5, 0, 0.5, 1, 0.333333333, 0, 0.5, 0.5, 0.5, 1, 0.666666667, 0.666666667, 0.333333333, 0, 1, 0, 0.666666667, 0, 0.666666667, 0.5, 1, 0.5, 0.5, 0.5, 0.5, 0, 0.666666667, 0.5, 0, 0, 1, 0, 1, 1, 0.5]
# }

data = {
    'Group': ['A', 'A', 'A', 'B', 'B', 'B', 'B', 'B', 'B', 'C', 'C', 'C', 'C', 'C', 'D', 'D', 'D', 'D', 'E', 'E', 'E', 'F', 'F', 'F', 'F', 'G', 'G', 'G', 'G', 'G', 'H', 'H', 'H', 'I', 'I', 'I', 'J', 'J', 'J', 'K', 'K', 'K', 'K', 'K', 'L', 'L', 'L', 'L'],
    'Rate': [0.666666666666667, 0.6, 1, 0.5, 0.666666666666667, 0, 0.75, 1, 0.666666666666667, 0.75, 0.666666666666667, 0, 1, 0.428571428571429, 0.75, 0.4, 1, 0.6, 1, 1, 1, 0.5, 0.666666666666667, 0.666666666666667, 1, 0.666666666666667, 1, 1, 1, 0.571428571428571, 0.666666666666667, 1, 1, 1, 1, 0.5, 0.8, 0.6, 1, 0.5, 0.5, 1, 1, 0, 0, 1, 1, 1]
}



df = pd.DataFrame(data)

# Estrai tutti i gruppi unici
groups = df['Group'].unique()

# Dizionario per memorizzare i risultati significativi
significant_results = {}

# Esegui il confronto tra ogni coppia di gruppi
for i in range(len(groups)):
    for j in range(i + 1, len(groups)):
        group_1 = groups[i]
        group_2 = groups[j]
        group_1_data = df[df['Group'] == group_1]['Rate']
        group_2_data = df[df['Group'] == group_2]['Rate']
        
        # Esegui il test di Mann-Whitney U
        u_statistic, p_value = mannwhitneyu(group_1_data, group_2_data, alternative='two-sided')
        
        # Memorizza i risultati se p-value < 0.05
        if p_value < 0.05:
            significant_results[(group_1, group_2)] = {'U-statistic': u_statistic, 'p-value': p_value}

# Mostra solo i risultati significativi
if significant_results:
    for groups_pair, result in significant_results.items():
        print(f"Confronto tra Gruppo {groups_pair[0]} e Gruppo {groups_pair[1]}:")
        print(f"U-statistic: {result['U-statistic']}, p-value: {result['p-value']}")
        print(f"Le differenze tra Gruppo {groups_pair[0]} e Gruppo {groups_pair[1]} sono statisticamente significative (p < 0.05)")
        print("--------")
else:
    print("Non ci sono differenze statisticamente significative tra i gruppi.")
