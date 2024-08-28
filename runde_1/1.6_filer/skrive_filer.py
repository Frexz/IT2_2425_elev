# Skrive til filer - man kan skrive innhold til fil med funksjonen write(). En fil blir opprettet
# hvis oppgitt filnavn ikke finnes i mappen, mens filen overskrives hvis filnavnet finnes. Vi oppgir
# mode='w' for å si fra at vi skrive til en fil, og har encoding='utf-8' slik at norske tegn aksepteres.
with open('norsk.txt', mode='w', encoding='utf-8') as fil:
    fil.write('1: EN\n2: TO\n3: TRE\n')
    fil.write('æ ø å Æ Ø Å')