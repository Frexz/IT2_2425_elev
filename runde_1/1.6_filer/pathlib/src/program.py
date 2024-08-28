from pathlib import Path

# Finner stien til mappen dette programmet ligger i
print(f'Mappesti til dette programmet: {Path(__file__).resolve().parent}')

# Finner stien til en fil som ligger i en annen mappe. Første .parent gir stien til src-mappen. 
# Neste .parent gir stien til pathlib-mappen. .joinpath tar stien til pathlib-mappen og legger
# til argumentene med \ mellom: ...\pathlib\data\txt\filnavn.txt
fil = Path(__file__).resolve().parent.parent.joinpath('data', 'txt', 'filnavn.txt')

print(f'Filbane: {fil}')

# Åpner filen og leser den
with fil.open() as f:
    print(f.read())