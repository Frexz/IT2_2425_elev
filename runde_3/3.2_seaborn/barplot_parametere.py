"""
seaborn.barplot()-metoden har diverse parametere som kan være nyttige:

data - oppgi navn på DataFrame
x, y, hue - Oppgi kolonnenavn. hue grupperer stolpediagrammet på en kolonne
order - endrer rekkefølgen til stolpene
estimator - kan regne med diverse aggregat-funksjoner (sum, size, mean, min, max osv.)
errorbar - errorbar=None fjerne svart strek fra toppen av en stolpe
orient - orient='h' gir horisontale stolper (f.eks når etiketter på x-akse er lange)
palette - angi andre farge med en liste. Farger kan gis med navn ('red') eller med HEX-kode ('FF0000')
dodge - default er False og gjør at grupperte stolper står ved siden av hverandre. True stabler stolper i stedet.

"""
import seaborn as sns
import matplotlib.pyplot as plt

# Dette er et innebygd datasett i seaborn og er datasettet med tips vi har sett på før
df = sns.load_dataset("tips")
df.info()

# Total tips per ukedag
# set(title=) lager en tittel til diagrammet
sns.barplot(data=df, x='day', y='tip',
            estimator='sum', errorbar=None).set(title="Total tips fordelt på ukedager")
plt.show()

# Nå er stolpene ordnet med order-parameteren
sns.barplot(data=df, x='day', y='tip', 
            order=['Sat', 'Sun', 'Thur', 'Fri'],
            estimator='sum', errorbar=None).set(title="Total tips fordelt på ukedager")
plt.show()

# Dataene er nå gruppert etter røykere med parameteren hue
sns.barplot(data=df, x='day', y='tip', hue="smoker",
            order=['Sat', 'Sun', 'Thur', 'Fri'],
            estimator='sum', errorbar=None).set(title="Total tips fordelt på ukedager")
plt.show()

# Ved å fjerne estimator-parameteren viser diagrammet gjennomsnitt (da mean er default-verdien til estimator)
sns.barplot(data=df, x='day', y='tip', hue="smoker",
            order=['Sat', 'Sun', 'Thur', 'Fri'],
            errorbar=None).set(title="Total tips fordelt på ukedager")
plt.show()