import seaborn as sns
import matplotlib.pyplot as plt

df = sns.load_dataset("tips")

# Man kan sette en stil med sns.set_style(<stil>). Her er noen stiler:
# 'darkgrid' - mørk bakgrunn med hvite ruter
# 'whitegrid' - hvit bakgrunn med mørke ruter
# 'dark' - mørk bakgrunn
# 'white' - hvit bakgrunn
# 'ticks' - merker på tallinjen
sns.set_style('ticks')

# Man kan også justere størrelse på elementer med sns.set_context(<kontekst>)
# Kontekster fra liten til stor: 'paper', 'notebook', 'talk', 'poster'
sns.set_context('poster')

# Vi kan endre farger med palette-parameteren og bruke sns.color_palette() for å generere en palett
palette = sns.color_palette('Accent', 8, 0.7)

sns.barplot(data=df, x='day', y='tip',
            estimator='sum', errorbar=None,
            palette=palette).set(title="Total tips fordelt på ukedager")
plt.show()