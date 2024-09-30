import pandas as pd
import matplotlib.pyplot as plt

# Carica il file ODS
file_path = '/Users/simo/Desktop/magistrale/experiments/exp1/demo.ods'  # Sostituisci con il tuo percorso
df = pd.read_excel(file_path, engine='odf')

# Conta le occorrenze di ciascuna combinazione di RISK e ML
counts = df.groupby(['RISK', 'ML']).size().reset_index(name='count')

# Scatter plot: Asse X per RISK, Asse Y per ML, dimensione cerchi in base al numero di persone
plt.figure(figsize=(8, 6))
plt.scatter(counts['RISK'], counts['ML'], s=counts['count']*100, color='blue', alpha=0.6, edgecolor='black')

# Titolo e etichette degli assi
plt.title('Demographic Scatter Plot')
plt.xlabel('Risk-assessment exp')
plt.ylabel('ML-algorithms exp')

# Imposta un limite per assi per renderli più leggibili
plt.xticks([0, 1, 2, 3])
plt.yticks([0, 1, 2, 3])

# Mostra il grafico
plt.grid(True)
plt.show()
