from statistics import mean, median, mode

tall = [5, 3, 8, 11, 9, 3, 2]

# sum() - regner ut summer av alle elementene i listen
print(f'Sum: {sum(tall)}')

# max() - finner største tall i listen
print(f'Størst: {max(tall)}')

# min() - finner minste tall i listen
print(f'Minst: {min(tall)}')

# mean() - finner gjennomsnitt av alle tallene i listen
print(f'Gjennomsnitt: {mean(tall)}')

# median() - finner medianen til alle tallene i listen
print(f'Median: {median(tall)}')

# mode() - finner typetallet i listen
print(f'Typetall: {mode(tall)}')