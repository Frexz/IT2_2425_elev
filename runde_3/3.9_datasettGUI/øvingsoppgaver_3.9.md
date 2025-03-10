# Øvingsoppgaver 3.9 - Datasett med GUI

# 3.9.1
**Iris**-datasettet er et kjent datasett i maskinlæring og statistikk, som inneholder informasjon om 150 iris-blomster fordelt på tre arter: *Setosa*, *Versicolor* og *Virginicica*. For hver blomst er det målt fire egenskaper:

- *Sepal length*    (begerbladets lengde)
- *Sepal width*     (begerbladets bredde)
- *Petal length*    (kronbladets lengde)
- *Petal width*     (kronbladets bredde)

Lag et objektorientert program hvor brukeren kan velge mellom tre visninger.

1. Datasettet (hele tabellen)
2. Et stolpediagram med gjennomsnittlig *sepal length* per art
3. Et kakediagram over antall blomster i datasettet per art

Du kan lese inn datasettet med ```sns.load_dataset('iris')```, som krever internettilkobling, eller benytte vedlagte **iris.csv**.

# 3.9.2
**Titanic**-datasettet er et kjent datasett som inneholder informasjon om et utvalg av passasjerenne på det skjebnesvangre skipet RMS Titanic. For hver passasjer er det registrert flere opplysninger, blant annet

- *survived*    (overlevde: 0 = omkom, 1 = overlevde)
- *pclass*      (klasse)
- *sex*         (kjønn)
- *age*         (alder)
- *fare*        (billettpris i £)
- *embark_town* (avreisehavn)

Lag et objektorientert program hvor brukeren kan velge mellom tre visninger:

1. Brukeren skal kunne velge passasjerklasse fra en *combobox* (Alle, 1, 2, 3). Programmet skal deretter vise en tabell med passasjerene i den valgte klassen.
2. Brukeren skal kunne velge mellom to ulike diagrammer ved hjelp av radioknapper:

- Et stolpediagram som viser gjennomsnittlig billettpris per avreisehavn
- Et sektordiagram som viser fordelingen av overlevende og omkomne passasjerer.

Du kan lese inn datasettet med ```sns.load_dataset('titanic')```, som krever internettilkobling, eller benytte vedlagte **titanic.csv**.