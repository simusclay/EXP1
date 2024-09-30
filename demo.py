import pandas as pd
import matplotlib.pyplot as plt

# Carica il file ODS
file_path = '/Users/simo/Desktop/magistrale/experiments/exp1/demo.ods'  # Sostituisci con il tuo percorso
df = pd.read_excel(file_path, engine='odf')

# Conta le occorrenze di ciascun valore nella colonna 'RISK' e 'ML'
risk_counts = df['RISK'].value_counts().sort_index()
ml_counts = df['ML'].value_counts().sort_index()

# Crea i due istogrammi
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 6))

# Istogramma per RISK
ax1.bar(risk_counts.index, risk_counts.values, color='lightblue')
ax1.set_title('Risk-assessment exp')
ax1.set_xlabel('Expertise')
ax1.set_ylabel('Number of participants')
ax1.set_xticks([0, 1, 2, 3])  # Imposta i ticks sull'asse X

# Istogramma per ML
ax2.bar(ml_counts.index, ml_counts.values, color='lightgreen')
ax2.set_title('ML-algorithms exp')
ax2.set_xlabel('Expertise')
ax2.set_ylabel('Number of participants')
ax2.set_xticks([0, 1, 2, 3])  # Imposta i ticks sull'asse X

plt.tight_layout()
plt.show()

# Scatter plot per l'unione dei due istogrammi
