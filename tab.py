import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Dati di esempio per M1 e M2
data_M2 = [
    0.666666666666667, 0.6, 1, 0.5, 0.666666666666667, 
    0, 0.75, 1, 0.666666666666667, 0.75, 0.666666666666667, 
    0, 1, 0.428571428571429, 0.75, 0.4, 1, 0.6, 1, 1, 
    1, 0.5, 0.666666666666667, 0.666666666666667, 1, 
    0.666666666666667, 1, 1, 1, 0.571428571428571, 
    0.666666666666667, 1, 1, 1, 1, 0.5, 0.8, 0.6, 
    1, 0.5, 0.5, 1, 1, 0, 0, 1, 1, 1
]

data_M1 = [
    0.666666666666667, 1, 1, 0, 0.5, 0.666666666666667, 
    0.5, 0.666666666666667, 0.5, 0.666666666666667, 
    1, 0.333333333333333, 0.5, 0, 0.5, 1, 
    0.333333333333333, 0, 0.5, 0.5, 0.5, 1, 
    0.666666666666667, 0.666666666666667, 0.333333333333333, 
    0, 1, 0, 0.666666666666667, 0, 0.666666666666667, 
    0.5, 1, 0.5, 0.5, 0.5, 0.5, 0, 0.5, 
    0.666666666666667, 0.5, 0.666666666666667, 0, 
    0, 1, 0, 1, 0.5
]

# Gruppi di appartenenza
groups = [
    'A', 'A', 'A', 'B', 'B', 'B', 'B', 'B', 'B', 
    'C', 'C', 'C', 'C', 'C', 'D', 'D', 'D', 'D', 
    'E', 'E', 'E', 'F', 'F', 'F', 'F', 'G', 'G', 
    'G', 'G', 'G', 'H', 'H', 'H', 'I', 'I', 'I', 
    'J', 'J', 'J', 'K', 'K', 'K', 'K', 'K', 'L', 
    'L', 'L', 'L'
]

# Creazione del DataFrame
df = pd.DataFrame({
    'Group': groups,
    'M1': data_M1,
    'M2': data_M2
})

# Calcolo delle statistiche per ogni gruppo
result_df = df.groupby('Group').agg(
    meanM1=('M1', 'mean'),
    stddevM1=('M1', 'std'),
    medianM1=('M1', 'median'),
    meanM2=('M2', 'mean'),
    stddevM2=('M2', 'std'),
    medianM2=('M2', 'median')
).reset_index()

# Arrotonda i risultati a tre decimali
result_df = result_df.round(3)

# Creazione della figura
fig, ax = plt.subplots(figsize=(10, 6))

# Nascondi gli assi
ax.axis('tight')
ax.axis('off')

# Crea la tabella
table_data = result_df.values
table = ax.table(cellText=table_data, colLabels=result_df.columns, cellLoc='center', loc='center')

# Stile della tabella
table.auto_set_font_size(False)
table.set_fontsize(10)
table.scale(1.2, 1.2)

# Mostra la figura
plt.title('Statistiche per Gruppo')
plt.show()
