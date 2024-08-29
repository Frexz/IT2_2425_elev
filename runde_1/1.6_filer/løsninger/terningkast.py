from statistics import mean

with open('terningkast.txt') as fil:
    resultater = []
    for tall in fil:
        resultater.append(int(tall))
    
    gjennomsnitt = mean(resultater)
    print(f'Gjennomsnittet av alle resultatene er {gjennomsnitt}')