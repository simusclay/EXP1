import pandas as pd
from scipy.stats import mannwhitneyu

# Crea il DataFrame con i tuoi dati
# AI
# data = {
#     'Group': ['A', 'A', 'A', 'B', 'B', 'B', 'B', 'B', 'B', 'C', 'C', 'C', 'C', 'C', 'D', 'D', 'D', 'D', 'E', 'E', 'E', 'F', 'F', 'F', 'F', 'G', 'G', 'G', 'G', 'G', 'H', 'H', 'H', 'I', 'I', 'I', 'J', 'J', 'J', 'K', 'K', 'K', 'K', 'K', 'L', 'L', 'L', 'L'],
#     'Rate': [0.666666667, 1, 1, 0, 0.5, 0.666666667, 0.5, 0.666666667, 0.5, 0.666666667, 1, 0.333333333, 0.5, 0, 0.5, 1, 0.333333333, 0, 0.5, 0.5, 0.5, 1, 0.666666667, 0.666666667, 0.333333333, 0, 1, 0, 0.666666667, 0, 0.666666667, 0.5, 1, 0.5, 0.5, 0.5, 0.5, 0, 0.5, 0.666666667, 0.5, 0.666666667, 0, 0, 1, 0, 1, 0.5]
# }

# CI
data = {
    'Group': ['A', 'A', 'A', 'B', 'B', 'B', 'B', 'B', 'B', 'C', 'C', 'C', 'C', 'C', 'D', 'D', 'D', 'D', 'E', 'E', 'E', 'F', 'F', 'F', 'F', 'G', 'G', 'G', 'G', 'G', 'H', 'H', 'H', 'I', 'I', 'I', 'J', 'J', 'J', 'K', 'K', 'K', 'K', 'K', 'L', 'L', 'L', 'L'],
    'Rate': [0.666666666666667, 0.6, 1, 0.5, 0.666666666666667, 0, 0.75, 1, 0.666666666666667, 0.75, 0.666666666666667, 0, 1, 0.428571428571429, 0.75, 0.4, 1, 0.6, 1, 1, 1, 0.5, 0.666666666666667, 0.666666666666667, 1, 0.666666666666667, 1, 1, 1, 0.571428571428571, 0.666666666666667, 1, 1, 1, 1, 0.5, 0.8, 0.6, 1, 0.5, 0.5, 1, 1, 0, 0, 1, 1, 1]
}


df = pd.DataFrame(data)

# Estrai i gruppi da confrontare
group_A = df[df['Group'] == 'A']['Rate']
group_C = df[df['Group'] == 'B']['Rate']

groups = df['Group'].unique()

# Esegui il confronto tra A e ogni altro gruppo
results = {}
for group in groups:
    if group != 'A':
        group_data = df[df['Group'] == group]['Rate']
        u_statistic, p_value = mannwhitneyu(group_A, group_data, alternative='two-sided')
        results[group] = {'U-statistic': u_statistic, 'p-value': p_value}

# Mostra i risultati
for group, result in results.items():
    print(f"Confronto tra Gruppo A e Gruppo {group}:")
    print(f"U-statistic: {result['U-statistic']}, p-value: {result['p-value']}")
    if result['p-value'] < 0.05:
        print(f"Le differenze tra Gruppo A e Gruppo {group} sono statisticamente significative (p < 0.05)")
    else:
        print(f"Le differenze tra Gruppo A e Gruppo {group} NON sono statisticamente significative (p >= 0.05)")
    print("--------")