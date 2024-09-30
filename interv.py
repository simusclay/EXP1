import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

# Carica il primo file .ods
file_path1 = '/Users/simo/Desktop/magistrale/experiments/exp1/AH.ods'  # Sostituisci con il percorso reale del tuo primo file
df1 = pd.read_excel(file_path1, engine='odf')

# Carica il secondo file .ods
file_path2 = '/Users/simo/Desktop/magistrale/experiments/exp1/CI.ods'  # Sostituisci con il percorso reale del tuo secondo file
df2 = pd.read_excel(file_path2, engine='odf')

# Aggiungi una colonna con il calcolo H / (H + AI) per entrambi i file
df1['ratio'] = df1['rate']
df2['ratio'] = df2['rate']

# Crea la figura con 2 subplot affiancati
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(16, 6))

# Boxplot per il primo file
sns.boxplot(x='Unnamed: 0', y='ratio', data=df1, palette="pastel", ax=ax1)
ax1.set_title('IntervM1')
ax1.set_xlabel('Groups')
ax1.set_ylabel('Human-trust rate')

# Boxplot per il secondo file
sns.boxplot(x='Unnamed: 0', y='ratio', data=df2, palette="muted", ax=ax2)
ax2.set_title('BIAS')
ax2.set_xlabel('Groups')
ax2.set_ylabel('Resilience rate')

# Boxplot per il primo file con mediana
sns.boxplot(x='Unnamed: 0', y='ratio', data=df1, palette="pastel", ax=ax1)
ax1.set_title('HUMAN-TRUST')
ax1.set_xlabel('Groups')
ax1.set_ylabel('Human-trust rate')

print(np.mean(df2['rate']))


# Aggiungi il layout e mostra i grafici
plt.tight_layout()
plt.show()
