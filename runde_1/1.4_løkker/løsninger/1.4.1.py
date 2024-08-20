# Ytre løkke kjører 3 ganger, indre løkke kjører 2 ganger for hver gang i ytre løkke
# For hver gang i ytre løkken skrives ut verdien til i som er henholdsvis 1, 2, og 3.
# For hver gang i indre løkken skrive ut verden til i sammen med verdien til j som henholdsvis
# er (1, 1), (1, 2), (2, 1), (2, 2), (3, 1) og (3, 2) der første tall er verdien til i og andre tall
# er verdien til j.
for i in range(1, 4):
    print('i: ' + str(i))
    for j in range(1, 3):
        print('i: ' + str(i) + ' og j:' + str(j))